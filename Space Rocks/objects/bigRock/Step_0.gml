direction=180;

image_angle+=r;
currentSpeed*=1.0000151;
motion_set(direction,currentSpeed);
function checkIfTouching()
{
	if place_meeting(x,y,bigRock)
	{
		spawn();
	}
}
checkIfTouching();
function spawn()
{
	while true
	{
		x= random_range(1280,1800);
		y=random_range(-50, 780);
		if place_meeting(x,y,bigRock)
		{
			x= random_range(1280,1800);
			y=random_range(-50, 780);
		}
		else
		{
			break
		}
	}
}
if (x <= 0)
{
	x= random_range(1280,1800);
	y=random_range(-50, 780);
}
/*if place_meeting(x,y,bigRock)
{
	x= random_range(1280,1800);
	y=random_range(-50, 780);
}*/
if place_meeting(x,y,bullet)
{
	var b= instance_place(x,y,bullet);
	instance_create_layer(x,y,"Instances",miniRock);
	instance_create_layer(x,y,"Instances",tinyRock);
	instance_deactivate_object(b);
	spawn();
}
if place_meeting(x,y,megaBullets)
{
	var b= instance_place(x,y,megaBullets);
	instance_create_layer(x,y,"Instances",miniRock);
	instance_create_layer(x,y,"Instances",tinyRock);
	instance_deactivate_object(b);
	spawn();
}
if isPaused
{
	angle=image_angle;
	image_angle=0;
}
if !isPaused
{
	image_angle= angle+r;
	angle= image_angle;
	
}

	
	