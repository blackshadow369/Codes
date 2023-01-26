package main

import (
	"fmt"
	"html/template"
	"io"
	"net/http"
	"strconv"
	"strings"
	"time"
)

type First int
type Sixth int

func (m First) ServeHTTP(res http.ResponseWriter, req *http.Request) {

	fmt.Println("we are on the first page")
	//io.WriteString(res, "This is login page")
	http.Redirect(res, req, "/login/", http.StatusSeeOther)
	io.WriteString(res, "This is the first page")

}

func (m Sixth) ServeHTTP(res http.ResponseWriter, req *http.Request) {
	//Add entry form
	/*
		v1 := req.FormValue("Id")
		fmt.Println(v1)
		fmt.Fprint(res, "we are on sixth place ")
		current_time := time.Now()
		fmt.Println(current_time.Format("2006-January-02"))
	*/
	temp := template.Must(template.ParseFiles("Add Entry form.html"))
	//var vol := 5
	err := temp.ExecuteTemplate(res, "Add Entry form.html", nil)
	if err != nil {
		fmt.Print(err)
	}

}

type Seventh int

func (m Seventh) ServeHTTP(res http.ResponseWriter, req *http.Request) {

	time.Sleep(5 * time.Second)
	fmt.Println("here are the values of add entry")
	v1 := req.FormValue("id")
	current_time := time.Now()
	v2 := current_time.Format("2006-01-02")
	v3 := req.FormValue("title")
	v4 := req.FormValue("content")
	currenttime := time.Now()
	v5 := strings.Split(currenttime.String(), ".")
	fmt.Println(v1, v2, v3, v4, v5[0])

	db := Databasees()
	insert, err := db.Query("Insert into `training`.`diary` values (?,?,?,?,?);", v1, v2, v3, v4, v5[0])
	if err != nil {
		fmt.Println("Failed")
		fmt.Println(err)
	} else {
		fmt.Println("Successfully updated ")
		http.Redirect(res, req, "/login/AddEntry", http.StatusSeeOther)
	}
	temp1, _ := strconv.Atoi(v1)
	temp := Entries(temp1)
	temp = temp + 1
	inset := db.QueryRow("update user set No_of_entry = ? where Id = ?", temp, temp1)
	if err != nil {
		fmt.Println("update query error :", inset)
	}

	defer insert.Close()
	defer db.Close()

}

type Eight int

func (m Eight) ServeHTTP(res http.ResponseWriter, req *http.Request) {
	//Update Entry

	temp := template.Must(template.ParseFiles("Update Entry form.html"))
	//var vol := 5
	err := temp.ExecuteTemplate(res, "Update Entry form.html", nil)
	if err != nil {
		fmt.Print(err)
	}

}

type Nine int

func (m Nine) ServeHTTP(res http.ResponseWriter, req *http.Request) {
	v1 := req.FormValue("id")
	v4, _ := strconv.Atoi(v1)
	v2 := req.FormValue("title")
	v3 := req.FormValue("content")

	db := Databasees()
	row := db.QueryRow("update diary set Content = ? where id = ? and Title = ?;", v3, v4, v2)
	if row != nil {
		fmt.Println("here is Nine error:", row)
	}
	fmt.Println("Successfully updated ")
	http.Redirect(res, req, "/login/UpdateEntry", http.StatusSeeOther)
}

type Ten int

func (m Ten) ServeHTTP(res http.ResponseWriter, req *http.Request) {

	temp := template.Must(template.ParseFiles("Delete Entry form.html"))
	//var vol := 5
	err := temp.ExecuteTemplate(res, "Delete Entry form.html", nil)
	if err != nil {
		fmt.Print(err)
	}

}

type Eleven int

func (m Eleven) ServeHTTP(res http.ResponseWriter, req *http.Request) {
	v0 := req.FormValue("id")
	v1, _ := strconv.Atoi(v0)
	v2 := req.FormValue("title")

	db := Databasees()
	row := db.QueryRow("delete from diary where Id=? and Title=?;", v1, v2)
	if row != nil {
	}
	fmt.Println("Success my friend")
	http.Redirect(res, req, "/login/", http.StatusSeeOther)

	db.Close()
}

type Twelve int

func (m Twelve) ServeHTTP(res http.ResponseWriter, req *http.Request) {

	temp := template.Must(template.ParseFiles("Show Entry form.html"))
	//var vol := 5
	err := temp.ExecuteTemplate(res, "Show Entry form.html", nil)
	if err != nil {
		fmt.Print(err)
	}

}

type Details struct {
	D_id             string
	D_date           string
	D_title          string
	D_content        string
	D_timeofcreation string
}

type Thirteen int

func (m Thirteen) ServeHTTP(res http.ResponseWriter, req *http.Request) {

	v0 := req.FormValue("id")
	v1, _ := strconv.Atoi(v0)
	all := showdetails(v1)
	temp := template.Must(template.ParseFiles("Show Entry form.html"))
	temp.ExecuteTemplate(res, "Show Entry form.html", all)
}

func showdetails(v1 int) []Details {
	db := Databasees()
	rows, err := db.Query("select * from diary where id=?;", v1)
	if err != nil {
		fmt.Print("Here is show error:", err)
	}
	var all []Details
	for rows.Next() {
		var temp Details
		err := rows.Scan(&temp.D_id, &temp.D_date, &temp.D_title, &temp.D_content, &temp.D_timeofcreation)
		if err != nil {
			fmt.Println("Row error", err)
		}
		all = append(all, temp)
	}
	db.Close()
	return all
}
