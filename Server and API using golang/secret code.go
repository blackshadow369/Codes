package main

import (
	"crypto/sha1"
	"encoding/hex"
	"strconv"
	"strings"
	"time"
)

func secret_code() string {
	//to generate a unique code
	currenttime := time.Now()
	res1 := strconv.Itoa(id_generator())
	res2 := strings.Split(currenttime.String(), ".")
	res3 := "#" + res1 + "#" + res2[0]
	//fmt.Println(res3)

	h := sha1.Sum([]byte(res3))
	h1 := hex.EncodeToString(h[:])
	//fmt.Println("md5 :", h)
	//fmt.Println("there :", h1)
	return h1
}
