temperature = 50
if temperature > 80:#if statement structure
    print ("it's too hot!")
    print ("stay inside!")
elif temperature < 60:#else if
    print("its too cold!")
    print ("stay inside!")
else:
    print("enjoy the outdoors")    

    if temperature > 80 or temperature <60:#using an or statement to do the samw as the code above
        print("stay inside!")
    else:
        print ("enjoy the outdoors")

        temperature = 75
        forecast = "rainy"
        if temperature < 80 and forecast != "rainy":#using and statement
            print("go outside")
        else:
            print("stay inside")
            
forecast ="rainy"
if not forecast == "rainy":#use of not keyword
    print("go outside!")
else:
    print("stay inside")               