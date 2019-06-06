from django.db import models



class Asset(models.Model):
    assetID = models.IntegerField(primary_key=True)
    asset_name = models.CharField(max_length=250)
    volume = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.assetID


class Task(models.Model):
    taskID = models.IntegerField(primary_key=True)
    task_name = models.CharField(max_length=250)
    frequency = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.taskID



class Worker(models.Model):
    
    workerID = models.IntegerField(primary_key=True)
    worker_name = models.CharField(max_length=250)
    skillset = models.CharField(max_length=250)
    #tasks = models.ForeignKey(Task, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.workerID



