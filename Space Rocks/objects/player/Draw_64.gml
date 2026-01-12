
draw_set_color(c_white);
draw_set_font(SmallFont);
draw_text(32, 32, "Bullets: " + string(bulletAmount) + "                                    Speed:" + string(currentSpeed)+ "               Time:"+string( round(global.clock/60 )));
draw_set_color(c_white);
if isPaused=true
{
	draw_set_font(BigFont)
	draw_text(550, 250, "PAUSED");
	draw_text(450, 350, "Press R to Restart");
	draw_text(485, 400, "Press Q to Quit");
	draw_set_font(SmallFont);
	draw_text(32, 32, "Bullets: " + string(bulletAmount) + "                                    Speed:" + string(currentSpeed));
}

if place_meeting(playerFutureCoords[0],playerFutureCoords[1],bigRock)
{
	draw_set_font(BigFont)
	currentSpeed=0
	draw_text(550, 250, "GAME OVER");
	draw_text(450, 350, "Press R to Restart");
	draw_text(485, 400, "Press Q to Quit");
	draw_set_font(SmallFont);
	draw_text(32, 32, "Bullets: " + string(bulletAmount) + "                                    Speed:" + string(currentSpeed));
	
}
if place_meeting(playerFutureCoords[0],playerFutureCoords[1],tinyRock)
{
	draw_set_font(BigFont)
	currentSpeed=0
	draw_text(550, 250, "GAME OVER");
	draw_text(450, 350, "Press R to Restart");
	draw_text(485, 400, "Press Q to Quit");
	draw_set_font(SmallFont);
	draw_text(32, 32, "Bullets: " + string(bulletAmount) + "                                    Speed:" + string(currentSpeed));
}
if place_meeting(playerFutureCoords[0],playerFutureCoords[1],miniRock)
{
	draw_set_font(BigFont)
	currentSpeed=0
	draw_text(550,250, "GAME OVER");
	draw_text(450, 350, "Press R to Restart");
	draw_text(485, 400, "Press Q to Quit");
	draw_set_font(SmallFont);
	draw_text(32, 32, "Bullets: " + string(bulletAmount) + "                                    Speed:" + string(currentSpeed));
}

if bulletAmount=maxBullets
{
	draw_set_font(SmallFont);
	draw_text(800,32, "Press E to unleash special attack");
	draw_text(32, 32, "Bullets: " + string(bulletAmount) + "                                    Speed:" + string(currentSpeed));
}
else if bulletAmount != maxBullets && keyboard_check_pressed(ord("E"))
{
	draw_set_font(SmallFont);
	draw_text(800,32,"You don't have enough energy yet!");
	draw_text(32, 32, "Bullets: " + string(bulletAmount) + "                                    Speed:" + string(currentSpeed));
}





// bar position and size
var bar_x = 32;
var bar_y = 32;
var bar_width = 200;
var bar_height = 20;

// background
draw_set_color(c_black);
draw_rectangle(bar_x, bar_y, bar_x + bar_width, bar_y + bar_height, false);

// fill (based on bulletAmount/maxBullets)
var percent = bulletAmount / maxBullets;
draw_set_color(c_yellow);
draw_rectangle(bar_x, bar_y, bar_x + bar_width * percent, bar_y + bar_height, false);

// outline
draw_set_color(c_white);
draw_rectangle(bar_x, bar_y, bar_x + bar_width, bar_y + bar_height, true);

// text label
draw_set_color(c_white);
draw_text(bar_x, bar_y - 20, "Bullets: " + string(bulletAmount));