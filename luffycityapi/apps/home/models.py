from luffycityapi.utils.models import models, BaseModel


# Create your models here.


class Nav(BaseModel):
    """导航菜单"""
    # 字段选项
    # 模型对象.<字段名>  ---> 实际数据
    # 模型对象.get_<字段名>_display()  --> 文本提示
    POSITION_OPTION = (
        # (实际数据, "文本提示"),
        (0, "顶部导航"),
        (1, "脚部导航"),
    )
    link = models.CharField(max_length=255, verbose_name="导航连接")
    is_http = models.BooleanField(default=False, verbose_name="是否是外部链接")
    position = models.IntegerField(choices=POSITION_OPTION, default=0)

    class Meta:
        db_table = "lf_nav"
        verbose_name = "导航菜单"
        verbose_name_plural = verbose_name
        app_label = 'home'
