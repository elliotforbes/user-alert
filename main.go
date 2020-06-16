package main

import (
	"fmt"

	"github.com/gofiber/fiber"
	rpio "github.com/stianeikeland/go-rpio/v4"
)

func SetupBoard() {
	err := rpio.Open()
	if err != nil {
		fmt.Println(err)
	}
	pin := rpio.Pin(10)
	pin.Output() // Output mode
	pin.High()
}

func main() {
	fmt.Println("User Alert System")

	SetupBoard()

	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) {
		c.Send("Hello, World!")
	})

	app.Listen(3000)
}
