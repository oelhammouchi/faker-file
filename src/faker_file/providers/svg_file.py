import os
from typing import Optional

import imgkit
from faker.providers import BaseProvider

from ..base import FileMixin, StringValue
from ..constants import DEFAULT_IMAGE_MAX_NB_CHARS
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("SvgFileProvider",)


class SvgFileProvider(BaseProvider, FileMixin):
    """SVG file provider.

        Usage example:

        from faker_file.providers.svg_file import SvgFileProvider

        file = SvgFileProvider(None).svg_file()

    Usage example with options:

        from faker_file.providers.svg_file import SvgFileProvider

        file = SvgFileProvider(None).svg_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = SvgFileProvider(Faker()).svg_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )
    """

    extension: str = "svg"

    def svg_file(
        self: "SvgFileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate an SVG file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        filename = storage.generate_filename(
            prefix=prefix,
            extension=self.extension,
        )

        tmp_filename = storage.generate_temporary_local_filename(
            prefix=prefix,
            extension=self.extension,
        )

        content = self._generate_text_content(
            max_nb_chars=max_nb_chars,
            wrap_chars_after=wrap_chars_after,
            content=content,
        )

        imgkit.from_string(
            f"<pre>{content}</pre>", tmp_filename, options={"quiet": ""}
        )

        with open(tmp_filename, "rb") as _file:
            storage.write_bytes(filename, _file.read())

        os.remove(tmp_filename)  # Clean up temporary files

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = {"content": content}
        return file_name
