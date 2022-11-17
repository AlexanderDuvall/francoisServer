package main

import (
	"fmt"
	"net/http"
	"os/exec"
)

func main() {
	http.HandleFunc("/getData", func(writer http.ResponseWriter, request *http.Request) {
		_ = request.ParseForm()
		request.Form.Get("...")
		body := request.Body
		fmt.Println(body)

		cmd := exec.Command("", "test.py")
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
	http.ListenAndServe("127.0.0.1:80", nil)

}
