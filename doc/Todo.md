# December tasks:

## Goal:

* Try to get to completed EC2 container with Postgres and back end for now.

## Tasks:

* [x] Test stack without key. Works!
* [x] Test ECS optimized EC2 instance.  Got it working but note that I don't see a way to wire this up to ECS trivially, since ECS wants to manage instances itself.  Also note that by default one cannot connect to such an instance.

## Notes for ECS Cluster:

AWS::ECS::Cluster
    AWS::AWS::ECS::CapacityProvider
        - AutoScalingGroupProvider
            AutoScalingGroupArn --> See below AWS::AutoScaling::AutoScalingGroup
        - ManagedScaling

AWS::AutoScaling::AutoScalingGroup
    AWS::EC2::LaunchTemplate (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html)
        Image ID goes here.  See EC2.yml
        AWS::EC2::LaunchTemplate LaunchTemplateData
    AWS::AutoScaling::AutoScalingGroup MixedInstancesPolicy - This and instances distribution determine # of on-demand, spot, reserved, etc.
        - AWS::AutoScaling::AutoScalingGroup InstancesDistribution