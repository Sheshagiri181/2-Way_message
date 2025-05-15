package main

import (
	"bufio"
	"fmt"
	"net"
)

func main() {
	// Listen on TCP port 12345 on all available interfaces
	ln, err := net.Listen("tcp", ":1235")
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	defer ln.Close()
	fmt.Println("Server is listening on port 1235...")
	// connecting
	conn, err := ln.Accept()
	if err != nil {
		fmt.Println("Error accepting connection:", err)
		return
	}
	defer conn.Close()
	fmt.Println("Client connected:", conn.RemoteAddr())
	// Read messages
	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		message := scanner.Text()
		fmt.Println("Received:", message)
		if message == "exit" {
			break
		}
	}
	fmt.Println("Connection closed.")
}


package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)
func main() {
	// Replace with the server's IP address
	serverIP := "---------------" // Example IP
	conn, err := net.Dial("tcp", serverIP)
	if err != nil {
		fmt.Println("Error connecting to server:", err)
		return
	}
	defer conn.Close()
	fmt.Println("Connected to server at", serverIP)
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print("Send: ")
		text, _ := reader.ReadString('\n')
		if _, err := conn.Write([]byte(text)); err != nil {
			fmt.Println("Error sending:", err)
			break
		}
		if text == "exit\n" {
			break
		}
	}
}