var currentSpeed;
var playerFutureCoords;
globalvar playerFutureCoords;
global.clock+=1;
if keyboard_check_pressed(vk_escape) 
{
    if (!isPaused) {
		preSpeed= currentSpeed
        currentSpeed = 0;
        isPaused = true;
	}
			
     else {
        currentSpeed = preSpeed;
        isPaused = false;
    }
}
if keyboard_check_pressed(ord("R")) game_restart();
if keyboard_check_pressed(ord("Q")) game_end();
playerFutureCoords=[x + lengthdir_x(0.1, direction), y + lengthdir_y(0.1,direction)];
image_angle= 0
if place_meeting(playerFutureCoords[0],playerFutureCoords[1],bigRock)
{
	
}
if place_meeting(playerFutureCoords[0],playerFutureCoords[1],tinyRock)
{
	room_goto(0);
}
if place_meeting(playerFutureCoords[0],playerFutureCoords[1],miniRock)
{
	room_goto(0);
}
if bulletAmount== 10
{
	if keyboard_check_pressed(ord("E"))
	{
		instance_create_layer(x,y,"Instances", megaBullet)
		bulletAmount=0
		
	}
	else
	{

	}
}

	
if keyboard_check(vk_up)
{
	speed=6;
	direction=image_angle+90;
}
if keyboard_check(vk_down)
{
	speed=6;
	direction=image_angle-90;	
}

if speed>0.1 && !(keyboard_check(vk_up)||(keyboard_check(vk_down)))
{
	speed*=0.90;
}
if speed<=0.1 && !(keyboard_check(vk_up)||(keyboard_check(vk_down)))
{
	speed=0;
}
	
if keyboard_check_pressed(vk_space) && !isPaused
{
	instance_create_layer(x,y,"Instances",bullet);
}
	
