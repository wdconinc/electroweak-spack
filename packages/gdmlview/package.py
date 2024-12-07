# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Gdmlview(CMakePackage):
    """xFSimple gdml viewer based on the Geant4 libraries."""

    homepage = "https://github.com/JeffersonLab/gdmlview"
    url      = "https://github.com/JeffersonLab/gdmlview/archive/refs/tags/v0.4.tar.gz"
    git      = "https://github.com/JeffersonLab/gdmlview.git"

    maintainers = ['wdconinc']

    version('main', branch='main', preferred=True)
    version('0.4', sha256='343ce7652418317e7e22d9edf8a99f90d0f65fb564da6e601399070b1d59a3a0')

    depends_on('boost +program_options')
    depends_on('geant4 +opengl')
