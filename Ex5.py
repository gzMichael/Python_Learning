name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

inch_to_cm=27.94
lbs_to_kg=0.453

height2= height * inch_to_cm
weight2= weight * lbs_to_kg

print ("Let's talk about %s." % name )
print ("He's %d inches (or %d cm) tall." % (height ,height2) )
print ("He's %d pounds (or %d kg) heavy." % (weight ,weight2) )
print ("Actually that's not too heavy." )
print ("He's got %s eyes and %s hair." % (eyes, hair))
print ("His teeth are usually %s depending on the coffee." % teeth)
# this line is tricky, try to get it exactly right)
print ("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))