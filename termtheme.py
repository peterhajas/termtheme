#!/usr/bin/python
import sys, os
import argparse
from color import Color

argumentParser = argparse.ArgumentParser()
argumentParser.add_argument('-t', '--color-theme', help='Path to the color theme to use when generating app themes', metavar='THEME', dest='themepath')
argumentParser.add_argument('-a', '--app', help='Name of the app to generate a theme for', metavar='APP', dest='app')

arguments = argumentParser.parse_args()

themepath = arguments.themepath
app = arguments.app

def contentsOfPath(path):
    handle = open(path, 'r')
    contents = handle.read()
    handle.close()
    return contents

def themeMapPathForApp(appName):
    # Look in our directory
    searchDir = os.getcwd()
    candidatePath = os.path.join(searchDir, appName + '.termthememap')
    return candidatePath

def themeMapForApp(appName):
    path = themeMapPathForApp(appName)
    contents = contentsOfPath(path)
    return contents

def themeContents(path):
    contents = contentsOfPath(path)
    return contents

def _colorsMatchingString(contents, string):
    numberedContents = [ ]
    for line in contents.split('\n'):
        if line.find(string) != -1:
            item = line.split(' ')[1]
            item = Color(hexStr=item)
            numberedContents.append(item)
    return numberedContents

def contentColorsForThemeContents(theme):
    return _colorsMatchingString(theme, 'content')

def accentColorsForThemeContents(theme):
    return _colorsMatchingString(theme, 'accent')

def backgroundColorsForThemeContents(theme):
    return _colorsMatchingString(theme, 'bg')

def themeForApp(themepath, app):
    themeMap = themeMapForApp(app)
    theme = themeContents(themepath)

    contentColors = contentColorsForThemeContents(theme)
    accentColors = accentColorsForThemeContents(theme)
    backgroundColors = backgroundColorsForThemeContents(theme)

    return None

