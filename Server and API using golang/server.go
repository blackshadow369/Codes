package main

import (
	"fmt"
	"net/http"
	//"net/http"
)

//init()

func main() {
	//to generate the unique id
	//test := id_generator()
	//generates a unique id each time
	//secret_code()
	//temp := Entries(1)
	//fmt.Println("Here is the no.of entries :", temp)
	//fmt.Println("here is unique id :", test)

	var firstpage First
	var login Second
	var register Third
	var info Forth
	var logauth Fifth
	var adde Sixth
	var add_entry_form Seventh
	var update_entry_form Eight
	var update_entry_form_success Nine
	var delete_entry_form Ten
	var delete_entry_form_success Eleven
	var show_entry_form Twelve
	var show_entry_form_success Thirteen

	mux := http.NewServeMux()
	mux.Handle("/", firstpage)
	mux.Handle("/login/", login)
	mux.Handle("/register/", register)
	mux.Handle("/info/", info)
	mux.Handle("/loginauth/", logauth)
	mux.Handle("/login/AddEntry", adde)
	mux.Handle("/login/AddEntry/success", add_entry_form)
	mux.Handle("/login/UpdateEntry", update_entry_form)
	mux.Handle("/login/UpdateEntry/success", update_entry_form_success)
	mux.Handle("/login/DeleteEntry", delete_entry_form)
	mux.Handle("/login/DeleteEntry/success", delete_entry_form_success)
	mux.Handle("/login/ShowEntry", show_entry_form)
	mux.Handle("/login/ShowEntry/success", show_entry_form_success)

	fmt.Println("We are on the server ")

	http.ListenAndServe(":8080", mux)

}
