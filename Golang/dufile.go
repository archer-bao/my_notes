package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/http/cookiejar"
	"os"
	"strings"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("params error")
		return
	}

	id := os.Args[1]
	id = id[strings.LastIndex(id, "/")+1 : strings.LastIndex(id, ".")]
	// fmt.Println(id)
	// return

	var client http.Client
	jar, err := cookiejar.New(nil)
	if err != nil {
		panic(err)
	}
	client.Jar = jar

	_, err = client.Get("http://dufile.com/")
	if err != nil {
		fmt.Printf("!!! %v\n", err)
		return
	}
	// resp.Body.Close()

	resp2, err := client.Get("http://dufile.com/downcode.php")
	if err != nil {
		fmt.Printf("@@@ %v\n", err)
		return
	}
	body, err := ioutil.ReadAll(resp2.Body)
	if err != nil {
		fmt.Printf("$$$ %v\n", err)
		return
	}
	err = ioutil.WriteFile("code.png", body, 0644)
	if err != nil {
		fmt.Printf("### %v\n", err)
		return
	}

	text := ""
	fmt.Println("Please enter verify code: ")
	_, err = fmt.Scanln(&text)
	if err != nil {
		fmt.Printf("input error%v\n", err)
		return
	}
	_, err = client.Post("http://dufile.com/downcode.php",
		"application/x-www-form-urlencoded", strings.NewReader("action=yz&id="+id+"&code="+text))
	if err != nil {
		fmt.Printf("%v\n", err)
		return
	}

	resp3, err := client.Get("http://dufile.com/dd.php?file_key=" + id + "&p=0")
	if err != nil {
		fmt.Printf("%v\n", err)
		return
	}

	bodyres, err := ioutil.ReadAll(resp3.Body)
	if err != nil {
		fmt.Printf("%v\n", err)
		return
	}
	pos1 := strings.Index(string(bodyres), `href="http://`)
	if pos1 == -1 {
		fmt.Println("no address 1")
		return
	}
	pos2 := strings.Index(string(bodyres), `点击普通下载`)
	if pos2 == -1 {
		fmt.Println("no address 2")
		return
	}
	address := string(bodyres)[pos1+6 : pos2-2]
	name := address[:strings.Index(address, "?")]
	name = name[strings.LastIndex(name, "/")+1:]
	fmt.Println(name)

	download, err := client.Get(address)
	file, err := ioutil.ReadAll(download.Body)
	err = ioutil.WriteFile(name, file, 0644)
	if err != nil {
		fmt.Printf("%v\n", err)
		return
	}
	return
}
