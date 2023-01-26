package main

import (
	"fmt"
	"html/template"
	"net/http"
)

// creating a method so that we can use it as a handler
type Second int

func (m Second) ServeHTTP(res http.ResponseWriter, req *http.Request) {
	//fmt.Println(http.StatusFound)
	fmt.Println("We are on the second page")
	//io.WriteString(res, "This is second page")

	//to execute the html file

	temp := template.Must(template.ParseFiles("Secondpage login.html"))
	//var vol := 5
	err := temp.ExecuteTemplate(res, "Secondpage login.html", nil)
	if err != nil {
		fmt.Print(err)
	}

}
