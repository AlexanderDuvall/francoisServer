package main

import (
	"fmt"
	"net/http"
	"os"
	"os/exec"
)

func main() {
	serverHandle := os.Args[1]
	pythonFile := os.Args[2]
	http.HandleFunc("/getData", func(writer http.ResponseWriter, request *http.Request) {
		_ = request.ParseForm()
		request.Form.Get("...")
		body := request.Body
		fmt.Println(body)

		cmd := exec.Command("", pythonFile)
		out, err := cmd.Output()
		if err != nil {
			panic(err)
		} else {
			fmt.Println(string(out))
		}
		fmt.Println()
		//writer.Write(out)
		fmt.Fprint(writer, string(out))
	})
	fmt.Println(serverHandle)
	http.ListenAndServe(serverHandle, nil)
}
