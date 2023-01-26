package main

import (
	"fmt"
	"html/template"
	"net/http"
)

type Content struct {
	Name  string
	Email string
	Date  string
	Code  string
	Id    int
	Error string
}

type Person struct {
	Name string
	Code string
}

type Third int
type Forth int
type Fifth int

func (m Third) ServeHTTP(res http.ResponseWriter, req *http.Request) {
	fmt.Println("We are on the third page")
	//io.WriteString(res, "We are on the third page")

	var temp *template.Template
	temp = template.Must(template.ParseFiles("Thirdpage register.html"))
	err := temp.ExecuteTemplate(res, "Thirdpage register.html", 32)
	if err != nil {
		fmt.Println(err)
	}
	var p Content
	p.Name = req.FormValue("Name")
	p.Email = req.FormValue("Email")
	p.Date = req.FormValue("Date")
	p.Code = secret_code()
	p.Id = id_generator()
	return

}

func (m Forth) ServeHTTP(res http.ResponseWriter, req *http.Request) {

	var p Content
	p.Name = req.FormValue("Name")
	p.Email = req.FormValue("Email")
	p.Date = req.FormValue("Date")
	p.Code = secret_code()
	p.Id = id_generator()

	db := Databasees()
	insert, err := db.Query("Insert into `training`.`user` values (?,?,?,?,?,0);", p.Id, p.Code, p.Name, p.Email, p.Date)
	if err != nil {
		fmt.Println("Failed")
		p.Error = "Error is here"

		fmt.Println(err)
	} else {
		fmt.Println("Success")
		var temp *template.Template
		temp = template.Must(template.ParseFiles("info show.html"))
		err := temp.ExecuteTemplate(res, "info show.html", p)
		if err != nil {
			fmt.Println(err)
		}
	}
	return
	defer insert.Close()
	defer db.Close()

}

func (m Fifth) ServeHTTP(res http.ResponseWriter, req *http.Request) {
	v1 := req.FormValue("n")
	v2 := req.FormValue("sc")
	//v3 := req.Method
	//fmt.Println("here is the answer :", v1, v2, v3)
	db := Databasees()
	rows, err := db.Query("select Name,Code from user;")
	if err != nil {
		fmt.Println("Erroe :", err)
	}
	var all []Person
	for rows.Next() {
		var temp Person
		err := rows.Scan(&temp.Name, &temp.Code)
		if err != nil {
			fmt.Println(err)
		}
		all = append(all, temp)
	}

	for _, value := range all {
		if value.Name == v1 && value.Code == v2 {
			var temp *template.Template
			temp = template.Must(template.ParseFiles("Options.html"))
			err = temp.ExecuteTemplate(res, "Options.html", nil)
			if err != nil {
				fmt.Println(err)
			}
			return
		}

	}
	var temp *template.Template
	temp = template.Must(template.ParseFiles("Secondpage login.html"))
	err = temp.ExecuteTemplate(res, "Secondpage login.html", nil)
	if err != nil {
		fmt.Println(err)
	}
	return
	defer rows.Close()
}
