const int out=13;
const int in=10;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(out,OUTPUT);
  pinMode(in,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  long dur;
  long dis;

  digitalWrite(out,LOW);
  delayMicroseconds(2);

  digitalWrite(out,HIGH);
  delayMicroseconds(10);
  digitalWrite(out,LOW);

  dur=pulseIn(in,HIGH);

  Serial.println(String(dur));

  delay(100);
}
