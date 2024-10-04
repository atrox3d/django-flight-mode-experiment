# Create your models here.

class DictMixin:
    def fieldnames(self):
        return [f.name for f in self._meta.get_fields()]

    def dict(self, *excluded:str):
        return {
            name:getattr(self, name) for name in self.fieldnames()
            if name not in excluded
        }