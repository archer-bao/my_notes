package main

import (
	"flag"
	"fmt"
	"io"
	"net/http"
	"os"
)

var (
	down       = ""
	up         = ""
	uploadPage = `<html>
	<head>
		<title>上传文件</title>
	</head>
	<body>
		</br></br>
		<form enctype="multipart/form-data" action="/upload" method="post">
		<input type="file" name="uploadfile" />
		<input type="hidden" name="token" value="{{.}}"/>
		<input type="submit" value="upload" />
		</form>
	</body>
	</html>`
)

// 处理/upload 逻辑
func upload(w http.ResponseWriter, r *http.Request) {
	fmt.Println("method:", r.Method) //获取请求的方法
	if r.Method == "GET" {
		fmt.Fprintf(w, uploadPage)
	} else {
		file, handler, err := r.FormFile("uploadfile")
		if err != nil {
			fmt.Println(err)
			fmt.Fprintf(w, "error")
			return
		}
		defer file.Close()
		fmt.Fprintf(w, "\n\n成功上传 %v", handler.Filename)
		f, err := os.OpenFile(up+handler.Filename, os.O_WRONLY|os.O_CREATE, 0666) // 此处假设当前目录下已存在test目录
		if err != nil {
			fmt.Println(err)
			fmt.Fprintf(w, "\n\n服务器保存文件失败")
			return
		}
		defer f.Close()
		io.Copy(f, file)
	}
}

func main() {
	flag.StringVar(&down, "d", "./", "specify download path, use current directory if not specify")
	flag.StringVar(&up, "u", "./", "specify upload path, use current directory if not specify")
	flag.Parse()
	fmt.Println("upload path:", up)
	fmt.Println("download path:", down)

	http.Handle("/", http.FileServer(http.Dir(down)))
	http.HandleFunc("/upload", upload)
	fmt.Println(http.ListenAndServe("0.0.0.0:8080", nil))
}
