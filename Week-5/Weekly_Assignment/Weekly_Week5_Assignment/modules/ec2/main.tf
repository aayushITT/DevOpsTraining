provider "aws" {
  region = "ap-south-1"

}
resource "aws_instance" "myec2" {
  instance_type   = var.instance_type
  ami             = var.ami_id
  security_groups = [aws_security_group.mySecurityGroup.name]

  tags = {
    Name = "myec2"
  }
 


  user_data = <<-EOF
#!/bin/bash
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
set -e

apt update -y
apt install -y apache2

systemctl enable apache2
systemctl start apache2

LAUNCH_TIME=$(date)
PRIVATE_IP=$(hostname -I | awk '{print $1}')
HOSTNAME=$(hostname)

cat <<EOF > /var/www/html/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Aayush Sharma's Static Web App</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(120deg, #4e54c8, #8f94fb);
            color: #fff;
            margin: 0;
            padding: 0;
        }
        header {
            padding: 20px;
            text-align: center;
            background: rgba(0,0,0,0.3);
        }
        main {
            padding: 40px;
            max-width: 800px;
            margin: auto;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }
        h1 {
            font-size: 2.5rem;
        }
        .info {
            margin-top: 30px;
            font-size: 1.2rem;
        }
        .info p {
            margin: 10px 0;
        }
        footer {
            text-align: center;
            padding: 15px;
            font-size: 0.9rem;
            background: rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>
    <header>
        <h1>🌐 Aayush Sharma's Static Web Application</h1>
        <p>Built with ❤️ on the Cloud</p>
    </header>
    <main>
        <div class="info">
            <p><strong>Hostname:</strong> $HOSTNAME</p>
            <p><strong>Private IP:</strong> $PRIVATE_IP</p>
            <p><strong>Launch Time:</strong> $LAUNCH_TIME</p>
        </div>
    </main>
    <footer>
        &copy; $(date +%Y) Aayush Sharma. All rights reserved.
    </footer>
</body>
</html>
EOF




       

}
resource "aws_security_group" "mySecurityGroup" {
  description = "Allow SSH and HTTP access"
  tags = {
    Name = "mySecurityGroup"
  }


  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}