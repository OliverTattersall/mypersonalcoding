//Annika Margie


// Variables 
int x = 1;
int y = 480;
int lineSubB = 0;
int lineSubG = 0;
int j = 0;
int stepSize = 5;

Lines [] lines = new Lines[100];

void setup()
{
  size(640, 480);
  background(0);
  blendMode(ADD);
  //noLoop();
  for (int i = 0; i <lines.length; i++){
   lines[i] = new Lines();
  }
}


void draw()
{
  noLoop();
  for (int i = 1; i < width; i = i + 15)// blue vertical lines 
  {
    lineSubB = lineSubB + 10;
    stroke(102, 153, 255);
    line (i, 1, i, 250 - lineSubB);
    stroke(102, 204, 255);
    line (i+7, 1, i+7, 300 - lineSubB);
  }

  for (int j = 0; j < width; j = j +15) // green vertical lines 
  {
    lineSubG = lineSubG + 10;
    stroke(42, 181, 56);
    line (j, 650 -lineSubG, j, 480); 
    stroke(128, 220, 118);
    line(j-7, 600 - lineSubG, j-7, 480);
  }
  stroke(0);

  for (int n = 0; n < width; n = n  + 35) // loop to make circles go from the bottom left to the top right
  {
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
  }
  myLine();
   
}

void myLine(){
  //loop();
  for (int i = 0; i <lines.length; i++){
    lines[i].fall();
    lines[i].show();
  }
}
