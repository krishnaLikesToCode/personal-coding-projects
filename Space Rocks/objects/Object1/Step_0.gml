if keyboard_check(vk_right)
{
    image_angle -= 1;
    show_debug_message("Rotating right, angle: " + string(image_angle));
}
else if keyboard_check(vk_left)
{
    image_angle += 1;
    show_debug_message("Rotating left, angle: " + string(image_angle));
}

if keyboard_check(vk_up)
{
    speed = 2;
    direction = image_angle;
    show_debug_message("Moving up - Speed: " + string(speed) + ", Direction: " + string(direction) + ", Position: " + string(x) + "," + string(y));
}
else if keyboard_check(vk_down)
{
    speed = 2;
    direction = image_angle + 180;
    show_debug_message("Moving down - Speed: " + string(speed) + ", Direction: " + string(direction) + ", Position: " + string(x) + "," + string(y));
}
else
{
    if speed > 0.1
    {
        speed *= 0.9;
    }
    else
    {
        speed = 0;
    }
}

// Force movement test - if this works, something else is blocking normal movement
if keyboard_check(vk_space)
{
    x += 1; // Direct coordinate change
    show_debug_message("Force moved to: " + string(x) + "," + string(y));
}