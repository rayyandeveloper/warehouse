from django.db import models



class File(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    


    def __str__(self):
        return self.name



class Folder(models.Model):
    name = models.CharField(max_length=200)
    files = models.ForeignKey(File, blank=True, on_delete=models.CASCADE)
    # folders = models.ForeignKey() keyinroq
    

    def __str__(self):
        return self.name





class Repository(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200)

    folders = models.ManyToManyField(Folder, blank=True)
    files = models.ManyToManyField(File, blank=True)


    def __str__(self):
        return self.name




