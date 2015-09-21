#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	C++ library for rendering OpenGL models stored in glTF format
Summary(pl.UTF-8):	Biblioteka C++ do renderowania modeli OpenGL zapisanych w formacie glTF
Name:		libgltf
Version:	0.0.2
Release:	5
License:	MPL v2.0
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/libgltf/%{name}-%{version}.tar.bz2
# Source0-md5:	d63a9f47ab048f5009d90693d6aa6424
URL:		http://www.libreoffice.org/
BuildRequires:	GLM >= 0.9.0.0
BuildRequires:	OpenGL-devel >= 3.0
BuildRequires:	boost-devel >= 1.41.0
BuildRequires:	glew-devel >= 1.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig >= 1:0.20
Requires:	OpenGL >= 3.0
Requires:	glew >= 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgltf is a C++ library for rendering OpenGL models stored in glTF
format.

The glTF, the GL Transmission Format, is the runtime asset format for
the GL APIs: WebGL, OpenGL ES, and OpenGL. glTF bridges the gap
between formats used by modeling tools and the GL APIs. You can read
more about the format in it's specification:
https://github.com/KhronosGroup/glTF/blob/schema/specification/README.md

libgltf provides methods to load the OpenGL scene from glTF format and
render it into an existing OpenGL context. libgltf also allows to
change the camera position so the scene can be displayed from
different points of view.

Summary, libgltf can be a good base of a glTF viewer.

%description -l pl.UTF-8
libgltf to biblioteka C++ do renderowania modeli OpenGL zapisanych w
formacie glTF.

glTF (GL Transmission Format - format transmisyjny GL) to format
danych uruchomieniowych dla API GL: WebGL, OpenGL ES oraz OpenGL. glTF
wypełnia lukę między formatami używanymi przez narzędzia modelujące
oraz API GL. Więcej o formacie można znaleźć w specyfikacji:
https://github.com/KhronosGroup/glTF/blob/schema/specification/README.md

libgltf udostępnia metody do wczytywania sceny OpenGL z formatu glTF
oraz renderowania jej w istniejącym kontekście OpenGL. Pozwala także
zmieniać położenie kamery, dzięki czemu scena może być wyświetlana z
innych punktów widzenia.

Podsumowując, libgltf może być dobrą podstawą dla przeglądarki glTF.

%package devel
Summary:	Header files for libgltf library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgltf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GLM >= 0.9.0.0
Requires:	glew-devel >= 1.8.0
Requires:	libstdc++-devel

%description devel
Header files for libgltf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgltf.

%package static
Summary:	Static libgltf library
Summary(pl.UTF-8):	Statyczna biblioteka libgltf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgltf library.

%description static -l pl.UTF-8
Statyczna biblioteka libgltf.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgltf-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README
%attr(755,root,root) %{_libdir}/libgltf-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgltf-0.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgltf-0.0.so
%{_includedir}/libgltf-0.0
%{_pkgconfigdir}/libgltf-0.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgltf-0.0.a
%endif
