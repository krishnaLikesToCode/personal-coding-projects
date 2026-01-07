direction=45;
image_angle+=r;
currentSpeed*=1.0000151;
motion_set(165,currentSpeed+1);
if place_meeting(x, y, bullet)
{
    var e = instance_place(x, y, bullet);
    if (e != noone)
	{
		if bulletAmount=10
		{
			bulletAmount=10
		}
		else
		{
			bulletAmount+=1;
		}
    }
    instance_destroy();        
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