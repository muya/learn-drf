from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field()
    title = serializers.CharField(required=False, max_length=100)
    code = serializers.CharField(widget=widgets.Textarea, max_length=100000)
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
                                       default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary of
        deserialized field values

        If this method isn't defined, deserializing data will simply return a
        dictionary of items
        """
        if instance:
            # update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.linenos = attrs.get('language', instance.language)
            instance.style = attrs.get('style', instance.style)
            return instance

        # create a new instance
        return Snippet(**attrs)
