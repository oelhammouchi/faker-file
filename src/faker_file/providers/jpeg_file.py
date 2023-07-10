from typing import Callable, Optional, Sequence, Tuple, Union, overload

from faker import Faker
from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.python import Provider

from ..base import DEFAULT_FORMAT_FUNC, BytesValue, StringValue
from ..constants import DEFAULT_IMAGE_MAX_NB_CHARS
from ..storages.base import BaseStorage
from .mixins.graphic_image_mixin import GraphicImageMixin
from .mixins.image_mixin import ImageMixin

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "GraphicJpegFileProvider",
    "JpegFileProvider",
)


class JpegFileProvider(BaseProvider, ImageMixin):
    """JPEG file provider.

        Usage example:

        from faker import Faker
        from faker_file.providers.jpeg_file import JpegFileProvider

        file = JpegFileProvider(None).jpeg_file()

    Usage example with options:

        file = JpegFileProvider(None).jpeg_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = JpegFileProvider(Faker()).jpeg_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )
    """

    extension: str = "jpg"

    @overload
    def jpeg_file(
        self: "JpegFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def jpeg_file(
        self: "JpegFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        **kwargs,
    ) -> StringValue:
        ...

    def jpeg_file(
        self: "JpegFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_IMAGE_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        format_func: Callable[
            [Union[Faker, Generator, Provider], str], str
        ] = DEFAULT_FORMAT_FUNC,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a JPEG file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :param format_func: Callable responsible for formatting template
            strings.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
        """
        return self._image_file(
            storage=storage,
            basename=basename,
            prefix=prefix,
            max_nb_chars=max_nb_chars,
            wrap_chars_after=wrap_chars_after,
            content=content,
            format_func=format_func,
            raw=raw,
            **kwargs,
        )


class GraphicJpegFileProvider(BaseProvider, GraphicImageMixin):
    """Graphic JPEG file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.jpeg_file import GraphicJpegFileProvider

        FAKER = Faker()
        FAKER.add_provider(GraphicJpegFileProvider)

        file = FAKER.graphic_jpeg_file()

    Usage example with options:

        file = FAKER.graphic_jpeg_file(
            prefix="zzz",
            size=(800, 800),
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = FAKER.graphic_jpeg_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            basename="yyy",
            size=(1024, 1024),
        )
    """

    extension: str = "jpg"
    image_format: str = "jpeg"

    @overload
    def graphic_jpeg_file(
        self: "GraphicJpegFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        size: Tuple[int, int] = (256, 256),
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
        raw: bool = True,
        **kwargs,
    ) -> BytesValue:
        ...

    @overload
    def graphic_jpeg_file(
        self: "GraphicJpegFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        size: Tuple[int, int] = (256, 256),
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        ...

    def graphic_jpeg_file(
        self: "GraphicJpegFileProvider",
        storage: Optional[BaseStorage] = None,
        basename: Optional[str] = None,
        prefix: Optional[str] = None,
        size: Tuple[int, int] = (256, 256),
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
        raw: bool = False,
        **kwargs,
    ) -> Union[BytesValue, StringValue]:
        """Generate a graphic JPEG file with random lines.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param basename: File basename (without extension).
        :param prefix: File name prefix.
        :param size: Image size in pixels.
        :param hue: Read more about
            ://faker.readthedocs.io/en/dev/providers/faker.providers.color.html
        :param luminosity: If given, the output string would be separated
             by line breaks after the given position.
        :param raw: If set to True, return `BytesValue` (binary content of
            the file). Otherwise, return `StringValue` (path to the saved
            file).
        :return: Relative path (from root directory) of the generated file
            or raw content of the file.
        """
        return self._image_file(
            image_format=self.image_format,
            storage=storage,
            basename=basename,
            prefix=prefix,
            size=size,
            hue=hue,
            luminosity=luminosity,
            raw=raw,
            **kwargs,
        )
