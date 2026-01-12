direction=0;
image_angle+=r;
currentSpeed*=1.0000151;
motion_set(195,currentSpeed+1);
if place_meeting(x, y, bullet)
{
    var b = instance_place(x, y, bullet);
    if (b != noone)
	{
		if bulletAmount=10
		{
			bulletAmount=10
		}
		else
		{
			bulletAmount+=1;
		}
        instance_destroy(b);
    }
    instance_destroy();        
}
if (x<0 || y<0 || y>720)
{
	instance_destroy(self);
}
if isPaused
{
	motion_set(195,0)
}
else
{
	motion_set(195,currentSpeed+1);
}


if place_meeting(x, y, megaBullets)
{
    var e = instance_place(x, y, megaBullets);
    if (e != noone)
	{
		if bulletAmount=10
		{
			bulletAmount=10
		}
		else
		{
		}
    }
    instance_destroy();        
}
	
