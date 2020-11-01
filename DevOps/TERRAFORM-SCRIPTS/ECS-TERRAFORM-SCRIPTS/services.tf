
module "alb" {
  source  = "terraform-aws-modules/alb/aws"
  version = "~> 5.0"
  
  name = "yo-alb"

  load_balancer_type = "application"

  vpc_id             = "${aws_vpc.main.id}"
  subnets            = ["${aws_subnet.main.id}"]
  security_groups    = ["${aws_security_group.load_balancers.id}"]
  
  access_logs = {
    bucket = "my-alb-logs"
  }

  target_groups = [
    {
      name_prefix      = "pref-"
      backend_protocol = "HTTP"
      backend_port     = 80
      target_type      = "instance"
    }
  ]

  #https_listeners = [
  #  {
  #    port               = 443
  #    protocol           = "HTTPS"
  #    certificate_arn    = "arn:aws:iam::123456789:server-certificate/cert-123456789"
  #    target_group_index = 0
  #  }
  #]

  http_tcp_listeners = [
    {
      port               = 80
      protocol           = "HTTP"
      target_group_index = 0
    }
  ]

  tags = {
    Environment = "Dev"
  }
}



#resource "aws_elb" "yo-elb" {
#    name = "yo-elb"
#    security_groups = ["${aws_security_group.load_balancers.id}"]
#    subnets = ["${aws_subnet.main.id}"]
#
#    listener {
#        lb_protocol = "http"
#        lb_port = 80
#
#        instance_protocol = "http"
#        instance_port = 8080
#    }

#    health_check {
#        healthy_threshold = 3
#        unhealthy_threshold = 2
#        timeout = 3
#        target = "HTTP:8080/path"
#        interval = 5
#    }

#    cross_zone_load_balancing = true
#}

resource "aws_ecs_task_definition" "yo-task" {
    family = "yo-cluster"
    container_definitions = "${file("task-definitions/yo-systems-task.json")}"
}

resource "aws_ecs_service" "yo-service" {
    name = "yo-service"
    cluster = "${aws_ecs_cluster.main.id}"
    task_definition = "${aws_ecs_task_definition.yo-systems-task.arn}"
    iam_role = "${aws_iam_role.ecs_service_role.arn}"
    desired_count = 2
    depends_on = ["aws_iam_role_policy.ecs_service_role_policy"]

    load_balancer {
        elb_name = "yo-alb"
        container_name = "yo-systems-task"
        container_port = 8080
    }
}
