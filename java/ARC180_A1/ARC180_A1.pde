//Annika Margie


// Variables
int x = 1;
int y = 480;
int lineSubB = 0;
int lineSubG = 0;
int i =1;
int j = 0;
int n = 0;
int stepSize = 5;
int count = 0;


void setup()
{
  size(640, 480);
  background(0);
  blendMode(ADD);
  //noLoop();
}


void draw() {
  try {
    Thread.sleep(50);
  }
  catch (InterruptedException e) {
    e.printStackTrace();
  }
  if (count%44!=0 ||count==0) {
    blendMode(ADD);
    lineSubB = lineSubB + 10;

    stroke(102, 153, 255);
    line (i, -20, i, 225 - lineSubB);
    stroke(102, 204, 255);
    line (i+7, -20, i+7, 275 - lineSubB);

    lineSubG = lineSubG + 10;
    stroke(42, 181, 56);
    line (j, 675 -lineSubG, j, 480);
    stroke(128, 220, 118);
    line(j-7, 625 - lineSubG, j-7, 480);
  } else {
    blendMode(DARKEST);
    stroke(0,0,0);
    fill(0,0,0);
    triangle(0,0,0,275,407,0);
    triangle(640,480,640,182,195,480);
    i=-15;
    j=-15;
    lineSubB=0;
    lineSubG=0;
    
    //noLoop();
  }

  if (count<20) {
    blendMode(ADD);
    stroke(0);
    //for (int n = 0; n < width; n = n  + 35) // loop to make circles go from the bottom left to the top right
    //{
    //randomized variables
    float col = random(255);
    float dist = random(5);
    float elliSize = random(10, 100);
    float elliDist = random(-100, 100);
    //three ellipses, each a differend colour (red, green, blue)

    fill(col, 0, 0);
    ellipse(x + n, y - 480*n/640 - elliDist, elliSize, elliSize);
    fill(0, col, 0);
    ellipse(x + n + dist, y - 480*n/640 - elliDist+ dist, elliSize, elliSize);
    fill(0, 0, col);
    ellipse(x + n + dist*2, y - 480*n/640 - elliDist + dist*2, elliSize, elliSize);
    //}
  }
  i = i+15;
  j=j+15;
  n = n+35;
  count=count+1;
}


//void draw()
//{


//  for (int i = 1; i < width; i = i + 15)// blue vertical lines
//  {
//    lineSubB = lineSubB + 10;
//    stroke(102, 153, 255);
//    line (i, 1, i, 250 - lineSubB);
//    stroke(102, 204, 255);
//    line (i+7, 1, i+7, 300 - lineSubB);
//  }

//  for (int j = 0; j < width; j = j +15) // green vertical lines
//  {
//    lineSubG = lineSubG + 10;
//    stroke(42, 181, 56);
//    line (j, 650 -lineSubG, j, 480);
//    stroke(128, 220, 118);
//    line(j-7, 600 - lineSubG, j-7, 480);
//  }
//  stroke(0);

//  for (int n = 0; n < width; n = n  + 35) // loop to make circles go from the bottom left to the top right
//  {
//    //randomized variables
//    float col = random(255);
//    float dist = random(5);
//    float elliSize = random(10, 100);
//    float elliDist = random(-100, 100);
//    //three ellipses, each a differend colour (red, green, blue)

//    fill(col, 0, 0);
//    ellipse(x + n, y - 480*n/640 - elliDist, elliSize, elliSize);
//    fill(0, col, 0);
//    ellipse(x + n + dist, y - 480*n/640 - elliDist+ dist, elliSize, elliSize);
//    fill(0, 0, col);
//    ellipse(x + n + dist*2, y - 480*n/640 - elliDist + dist*2, elliSize, elliSize);
//  }
//}





void drawFlower(float flowerX, float flowerY, float petalSize) {
  System.out.println(flowerX);
}
