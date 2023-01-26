package main

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

type Identifier struct {
	ID int
}

func Databasees() *sql.DB {
	//
	DB, err := sql.Open("mysql", "root:karan@tcp(localhost:3306)/training")

	if err != nil {
		fmt.Println(err.Error())
	}

	err = DB.Ping()
	if err != nil {
		fmt.Println("Error varifying connection with db.Ping")
		panic(err.Error())
	}

	/*
		//for inserting
		insert, err := db.Query("Insert into `training`.`user` values (1,'asf','asfsaf','as','1990-1-23',1)")
		if err != nil {
			fmt.Println("this is here ", err)
			panic(err.Error())
		}

		defer insert.Close()
	*/
	return DB
}

func id_generator() int {
	var products []Identifier
	db := Databasees()
	rows, err := db.Query("select Id from user order by Id")
	if err != nil {
	}
	for rows.Next() {
		var temp Identifier
		err := rows.Scan(&temp.ID)
		if err != nil {
			fmt.Println(err)
		}
		products = append(products, temp)
	}
	Value := 1
	if products == nil {
		return Value
	}
	for value, name := range products {
		if Value != name.ID {
			return Value
		}
		fmt.Println(value, name.ID)
		Value++
	}
	defer db.Close()
	defer rows.Close()
	return Value
}

func Entries(v int) int {
	db := Databasees()
	row := db.QueryRow("select No_of_entry from user where Id = ?", v)
	var temp int
	err := row.Scan(&temp)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("Value of temp in databases", temp)
	return temp
}
