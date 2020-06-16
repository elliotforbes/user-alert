package main

import (
	"fmt"

	"github.com/gofiber/fiber"
	rpio "github.com/stianeikeland/go-rpio/v4"
)

func main() {
	fmt.Println("User Alert System")

	err := rpio.Open()
	if err != nil {
		fmt.Println(err)
	}

	pin := rpio.Pin(17)
	pin.Output()

	app := fiber.New()
	pin.Low()
	toggle := false

	app.Get("/", func(c *fiber.Ctx) {
		if toggle {
			fmt.Println("Light On!")
			pin.High()
		} else {
			fmt.Println("light Off!")
			pin.Low()
		}

		toggle = !toggle

		c.Send("Hello, World!")
	})

	app.Listen(3000)
}
