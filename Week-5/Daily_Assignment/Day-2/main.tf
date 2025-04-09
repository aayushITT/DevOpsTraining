
resource "aws_vpc" "myvpc"{

cidr_block="10.0.0.0/16"
tags={
Name="myvpc"
}

}

resource "aws_subnet" "mypublicsubnet"{

cidr_block="10.0.1.0/24"
vpc_id=aws_vpc.myvpc.id
availability_zone="ap-south-1a"
map_public_ip_on_launch=true
tags={

Name="mysubnetpublic"

}




}
resource "aws_subnet" "myprivatesubnet"{

cidr_block="10.0.3.0/24"
availability_zone="ap-south-1b"
vpc_id=aws_vpc.myvpc.id
map_public_ip_on_launch=false
tags={

Name="mysubnetprivate"

}
}
resource "aws_internet_gateway" "myigw"{
vpc_id=aws_vpc.myvpc.id
tags={
Name="myigw"

}

}

resource "aws_route_table" "mypublicroute"{

vpc_id=aws_vpc.myvpc.id
route{
cidr_block="0.0.0.0/0"
gateway_id=aws_internet_gateway.myigw.id


}


tags={
Name="mypublicroute"
}

}

resource "aws_route_table" "myprivateroute"{

vpc_id=aws_vpc.myvpc.id



tags={
Name="myprivateroute"
}

}


resource "aws_route_table_association" "myrouteassociation"{
subnet_id=aws_subnet.mypublicsubnet.id
route_table_id=aws_route_table.mypublicroute.id


}

resource "aws_route_table_association" "myrouteassociation1"{
subnet_id=aws_subnet.myprivatesubnet.id
route_table_id=aws_route_table.myprivateroute.id


}

 

