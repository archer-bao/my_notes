package main

import (
	"bytes"
	"fmt"
	"net"
	"strconv"
	"sync"
	"time"

	"golang.org/x/crypto/ssh"
)

func main() {
	var waitGroup = new(sync.WaitGroup)

	for i := 15; i < 238; i++ {
		waitGroup.Add(1)
		go func(i int) {
			defer waitGroup.Done()
			config := &ssh.ClientConfig{
				User: "version",
				Auth: []ssh.AuthMethod{
					ssh.Password("xxxxxxx"),
				},
				Timeout: 5 * time.Second,
				HostKeyCallback: func(hostname string, remote net.Addr, key ssh.PublicKey) error {
					return nil
				},
			}
			client, err := ssh.Dial("tcp", "10.200.71."+strconv.Itoa(i)+":22", config)
			if err != nil {
				fmt.Println("version: 10.200.71."+strconv.Itoa(i), "failed")
				waitGroup.Add(1)
				go func(i int) {
					defer waitGroup.Done()
					config := &ssh.ClientConfig{
						User: "version",
						Auth: []ssh.AuthMethod{
							ssh.Password("2wsx@WSX"),
						},
						Timeout: 5 * time.Second,
						HostKeyCallback: func(hostname string, remote net.Addr, key ssh.PublicKey) error {
							return nil
						},
					}
					client, err := ssh.Dial("tcp", "10.200.71."+strconv.Itoa(i)+":22", config)
					if err != nil {
						fmt.Println("version: 10.200.71."+strconv.Itoa(i), "failed")
						return
					}

					session, err := client.NewSession()
					if err != nil {
						fmt.Println("version: 10.200.71."+strconv.Itoa(i), "failed")
						return
					}
					defer session.Close()

					var b bytes.Buffer
					session.Stdout = &b
					if err := session.Run("/usr/bin/whoami"); err != nil {
						fmt.Println("Failed to run: " + err.Error())
					}
					fmt.Println("version: 10.200.71."+strconv.Itoa(i), "2wsx@WSX success")
				}(i)
				return
			}

			session, err := client.NewSession()
			if err != nil {
				fmt.Println("version: 10.200.71."+strconv.Itoa(i), "failed")
				return
			}
			defer session.Close()

			var b bytes.Buffer
			session.Stdout = &b
			if err := session.Run("/usr/bin/whoami"); err != nil {
				fmt.Println("Failed to run: " + err.Error())
			}
			fmt.Println("version: 10.200.71." + strconv.Itoa(i) + "$Mgyq636 success")
		}(i)

	}
	waitGroup.Wait()
}
