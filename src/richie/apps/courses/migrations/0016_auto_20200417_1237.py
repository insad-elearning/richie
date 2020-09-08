# Generated by Django 2.2.12 on 2020-04-17 10:37

from django.db import migrations, models

import richie.apps.core.fields.multiselect


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0015_add_category_plugin_variant"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="persontitletranslation",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="persontitletranslation",
            name="master",
        ),
        migrations.RemoveField(
            model_name="person",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="person",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="person",
            name="person_title",
        ),
        migrations.AlterField(
            model_name="blogpostpluginmodel",
            name="variant",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inherit"),
                    ("glimpse", "Default"),
                    ("mini", "Mini"),
                    ("favorite", "Favorite"),
                ],
                help_text="Optional glimpse variant for a custom look.",
                max_length=50,
                null=True,
                verbose_name="variant",
            ),
        ),
        migrations.AlterField(
            model_name="coursepluginmodel",
            name="variant",
            field=models.CharField(
                blank=True,
                choices=[(None, "Inherit"), ("glimpse", "Default"), ("small", "small")],
                help_text="Optional glimpse variant for a custom look.",
                max_length=50,
                null=True,
                verbose_name="variant",
            ),
        ),
        migrations.AlterField(
            model_name="courserun",
            name="languages",
            field=richie.apps.core.fields.multiselect.MultiSelectField(
                choices=[
                    ("af", "Afrikaans"),
                    ("ar", "Arabic"),
                    ("ast", "Asturian"),
                    ("az", "Azerbaijani"),
                    ("bg", "Bulgarian"),
                    ("be", "Belarusian"),
                    ("bn", "Bengali"),
                    ("br", "Breton"),
                    ("bs", "Bosnian"),
                    ("ca", "Catalan"),
                    ("cs", "Czech"),
                    ("cy", "Welsh"),
                    ("da", "Danish"),
                    ("de", "German"),
                    ("dsb", "Lower Sorbian"),
                    ("el", "Greek"),
                    ("en", "English"),
                    ("en-au", "Australian English"),
                    ("en-gb", "British English"),
                    ("eo", "Esperanto"),
                    ("es", "Spanish"),
                    ("es-ar", "Argentinian Spanish"),
                    ("es-co", "Colombian Spanish"),
                    ("es-mx", "Mexican Spanish"),
                    ("es-ni", "Nicaraguan Spanish"),
                    ("es-ve", "Venezuelan Spanish"),
                    ("et", "Estonian"),
                    ("eu", "Basque"),
                    ("fa", "Persian"),
                    ("fi", "Finnish"),
                    ("fr", "French"),
                    ("fy", "Frisian"),
                    ("ga", "Irish"),
                    ("gd", "Scottish Gaelic"),
                    ("gl", "Galician"),
                    ("he", "Hebrew"),
                    ("hi", "Hindi"),
                    ("hr", "Croatian"),
                    ("hsb", "Upper Sorbian"),
                    ("hu", "Hungarian"),
                    ("hy", "Armenian"),
                    ("ia", "Interlingua"),
                    ("id", "Indonesian"),
                    ("io", "Ido"),
                    ("is", "Icelandic"),
                    ("it", "Italian"),
                    ("ja", "Japanese"),
                    ("ka", "Georgian"),
                    ("kab", "Kabyle"),
                    ("kk", "Kazakh"),
                    ("km", "Khmer"),
                    ("kn", "Kannada"),
                    ("ko", "Korean"),
                    ("lb", "Luxembourgish"),
                    ("lt", "Lithuanian"),
                    ("lv", "Latvian"),
                    ("mk", "Macedonian"),
                    ("ml", "Malayalam"),
                    ("mn", "Mongolian"),
                    ("mr", "Marathi"),
                    ("my", "Burmese"),
                    ("nb", "Norwegian Bokmål"),
                    ("ne", "Nepali"),
                    ("nl", "Dutch"),
                    ("nn", "Norwegian Nynorsk"),
                    ("os", "Ossetic"),
                    ("pa", "Punjabi"),
                    ("pl", "Polish"),
                    ("pt", "Portuguese"),
                    ("pt-br", "Brazilian Portuguese"),
                    ("ro", "Romanian"),
                    ("ru", "Russian"),
                    ("sk", "Slovak"),
                    ("sl", "Slovenian"),
                    ("sq", "Albanian"),
                    ("sr", "Serbian"),
                    ("sr-latn", "Serbian Latin"),
                    ("sv", "Swedish"),
                    ("sw", "Swahili"),
                    ("ta", "Tamil"),
                    ("te", "Telugu"),
                    ("th", "Thai"),
                    ("tr", "Turkish"),
                    ("tt", "Tatar"),
                    ("udm", "Udmurt"),
                    ("uk", "Ukrainian"),
                    ("ur", "Urdu"),
                    ("vi", "Vietnamese"),
                    ("zh-hans", "Simplified Chinese"),
                    ("zh-hant", "Traditional Chinese"),
                ],
                help_text="The list of languages in which the course content is available.",
                max_choices=50,
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="organizationpluginmodel",
            name="variant",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inherit"),
                    ("glimpse", "Default"),
                    ("card", "Card"),
                    ("row", "Row"),
                ],
                help_text="Optional glimpse variant for a custom look.",
                max_length=50,
                null=True,
                verbose_name="variant",
            ),
        ),
        migrations.AlterField(
            model_name="organizationsbycategorypluginmodel",
            name="variant",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inherit"),
                    ("glimpse", "Default"),
                    ("card", "Card"),
                    ("row", "Row"),
                ],
                help_text="Optional glimpse variant for a custom look.",
                max_length=50,
                null=True,
                verbose_name="variant",
            ),
        ),
        migrations.DeleteModel(
            name="PersonTitle",
        ),
        migrations.DeleteModel(
            name="PersonTitleTranslation",
        ),
    ]