class Lines{
 
 float xl = random(width);
 float yl = random(-200,100);
 float ylspeed = random(5);
 float len = random(5,15);
 
 void fall(){
   yl = yl +ylspeed;
   
   if ( yl > height)
   {
    yl = random(-200, -100); 
   }
 }
 
 void show(){
   stroke(255);
   line(xl,yl,xl,yl+len);
 }
 
}
