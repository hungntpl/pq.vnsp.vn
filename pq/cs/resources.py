from import_export import resources
from .models import cs

class CSResource(resources.ModelResource):
    class Meta:
        model = cs
        import_id_fields = ['CSNo']
        # batch_size = 10
        # fields = ('field1', 'field2', 'field3') # specify fields to import/export
        exclude = ('ASManJudgment',
                'ASManNote',
                'ASManDate',
                'PIManJudgment',
                'PIManNote',
                'QAManJudgment',
                'QAManNote',
                'QAManDate',
                'QCManJudgment',
                'QCManNote',
                'QCManDate',
                'PRManJudgment',
                'PRManNote',
                'PRManDate',
                'DGDJudgment',
                'DGDNote',
                'DGDManDate',
                'PCManJudgment',
                'PCManNote',
                'PCManDate',
                'ImageSPEC',
                'PIManDate',
                'LastUser',
                'LastimeUser',
            )