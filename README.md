# pi-microscope

The pi-microscope is a hobby project of mine where I design and program a digital microscope. The core of the microscope is a Raspberry Pi to run the application together with the Raspberry Pi camera module. To achieve magnification I use a spare macro-lens from the [Foldscope project](https://www.foldscope.com/), which in itself is amazing and you should check it out. The hardware are 3d-printed parts that allow me together with some stepper motors to move the camera around. 

The bill of materials is not complete, yet, as the project is still under development. Indeed, I am currently using stepper motors salvaged from an old fax machine -- so not really off the shelf material. Once the design is polished I will list a full bill of materials here. Here is what I have used so far: 
* [Raspberry Pi 4 Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
* [2 Adafruit motor controller HATs](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi)
* [A Pololu DRV8825 Stepper Motor Driver](https://www.pololu.com/product/2133)
* 3 stepper motors (salvaged from fax machine)
* A short piece of LED-strip for illumination of the sample. Any couple of LEDs (say 6 bright ones) will do really. 

Similarly the list of CAD drawings is not complete, as I will likely have to adjust the frame to off the shelf motors. I do include the CAD drawings anyways, as not all of them are specific to the motors and they might be of use in your own design. I will update the drawing files as I go along.

Here are some images of the current iteration and a screenshot of the UI showing the microscope in action.
