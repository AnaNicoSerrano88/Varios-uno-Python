import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import askyesno
from tkinter.font import Font
import ctypes
import shutil
import glob
import os
import re
import requests
import xml.etree.cElementTree as ET
import datetime

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
data= os.getcwd()
provicional='Log_Provicional'

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry(f'{ancho}x{alto}')

info = tk.StringVar()
info.set('Open a file')

name_test = []
result = []
notest = 'NO TEST'
test_FFT = 'Final Functional Test'
runIn = 'RunIn'

def archivos_txt():
    # FFT.UpdateCr50Firmware.UpdateCR50Firmware
    UpdateCr50Firmware = glob.glob(f'{data}\\tests\\FFT.UpdateCr50Firmware.UpdateCR50Firmware-*')
    result_UpdateCr50Firmware = 'FAILED'
    for up in UpdateCr50Firmware:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\UpdateCr50Firmware-metadata.txt')
    try:
        with open('result\\UpdateCr50Firmware-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_UpdateCr50Firmware = 'PASSED'
        name_test.append('UpdateCr50Firmware.UpdateCR50Firmware')
        result.append([result_UpdateCr50Firmware,result_UpdateCr50Firmware])
        # print('UpdateCr50Firmware: '+result_UpdateCr50Firmware)
    except:
        name_test.append('UpdateCr50Firmware.UpdateCR50Firmware')
        result.append([result_UpdateCr50Firmware,notest])

    # FFT.UpdateCr50Firmware.RebootStep
    RebootStep = glob.glob(f'{data}\\tests\\FFT.UpdateCr50Firmware.RebootStep-*')
    result_RebootStep = 'FAILED'
    for up in RebootStep:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RebootStep-metadata.txt')
    try:
        with open('result\\RebootStep-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RebootStep = 'PASSED'
        name_test.append('UpdateCr50Firmware.RebootStep')
        result.append([result_RebootStep,result_RebootStep])
        # print('RebootStep: '+result_RebootStep)
    except:
        name_test.append('UpdateCr50Firmware.RebootStep')
        result.append([result_RebootStep,notest])

    # FFT.FFTStart.Start
    Start = glob.glob(f'{data}\\tests\\FFT.FFTStart.Start-*')
    result_Start = 'FAILED'
    for up in Start:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\Start-metadata.txt')
    try:
        with open('result\\Start-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_Start = 'PASSED'
        name_test.append('FFTStart.Start')
        result.append([result_Start,result_Start])
        # print('Start: '+result_Start)
    except:
        name_test.append('FFTStart.Start')
        result.append([result_Start,notest])

    # FFT.FFTStart.CheckImageVersion
    CheckImageVersion = glob.glob(f'{data}\\tests\\FFT.FFTStart.CheckImageVersion-*')
    result_CheckImageVersion = 'FAILED'
    for up in CheckImageVersion:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\CheckImageVersion-metadata.txt')
    try:
        with open('result\\CheckImageVersion-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_CheckImageVersion = 'PASSED'
        name_test.append('FFTStart.CheckImageVersion')
        result.append([result_CheckImageVersion,result_CheckImageVersion])
        # print('CheckImageVersion: '+result_CheckImageVersion)
    except:
        name_test.append('FFTStart.CheckImageVersion')
        result.append([result_CheckImageVersion,notest])

    # FFT.FFTStart.ReadDeviceDataFromVPD
    ReadDeviceDataFromVPD = glob.glob(f'{data}\\tests\\FFT.FFTStart.ReadDeviceDataFromVPD-*')
    result_ReadDeviceDataFromVPD = 'FAILED'
    for up in ReadDeviceDataFromVPD:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\ReadDeviceDataFromVPD-metadata.txt')
    try:
        with open('result\\ReadDeviceDataFromVPD-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_ReadDeviceDataFromVPD = 'PASSED'
        name_test.append('FFTStart.ReadDeviceDataFromVPD')
        result.append([result_ReadDeviceDataFromVPD,result_ReadDeviceDataFromVPD])
        # print('ReadDeviceDataFromVPD: '+result_ReadDeviceDataFromVPD)
    except:
        name_test.append('FFTStart.ReadDeviceDataFromVPD')
        result.append([result_ReadDeviceDataFromVPD,notest])

    # FFT.FFTStart.SetRegion
    SetRegion = glob.glob(f'{data}\\tests\\FFT.FFTStart.SetRegion-*')
    result_SetRegion = 'FAILED'
    for up in SetRegion:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\SetRegion-metadata.txt')
    try:
        with open('result\\SetRegion-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_SetRegion = 'PASSED'
        name_test.append('FFTStart.SetRegion')
        result.append([result_SetRegion,result_SetRegion])
        # print('SetRegion: '+result_SetRegion)
    except:
        name_test.append('FFTStart.SetRegion')
        result.append([result_SetRegion,notest])

    # FFT.FFTStart.SetModelName
    SetModelName = glob.glob(f'{data}\\tests\\FFT.FFTStart.SetModelName-*')
    result_SetModelName = 'FAILED'
    for up in SetModelName:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\SetModelName-metadata.txt')
    try:
        with open('result\\SetModelName-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_SetModelName = 'PASSED'
        name_test.append('FFTStart.SetModelName')
        result.append([result_SetModelName,result_SetModelName])
        # print('SetModelName: '+result_SetModelName)
    except:
        name_test.append('FFTStart.SetModelName')
        result.append([result_SetModelName,notest])
        
    # FFT.FFTStart.SetMLB
    SetMLB = glob.glob(f'{data}\\tests\\FFT.FFTStart.SetMLB-*')
    result_SetMLB = 'FAILED'
    for up in SetMLB:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\SetMLB-metadata.txt')
    try:
        with open('result\\SetMLB-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_SetMLB = 'PASSED'
        name_test.append('FFTStart.SetMLB')
        result.append([result_SetMLB,result_SetMLB])    
        # print('SetMLB: '+result_SetMLB)
    except:
        name_test.append('FFTStart.SetMLB')
        result.append([result_SetMLB,notest]) 

    # FFT.FFTStart.WriteDeviceDataToVPD
    WriteDeviceDataToVPD = glob.glob(f'{data}\\tests\\FFT.FFTStart.WriteDeviceDataToVPD-*')
    result_WriteDeviceDataToVPD = 'FAILED'
    for up in WriteDeviceDataToVPD:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\WriteDeviceDataToVPD-metadata.txt')
    try:
        with open('result\\WriteDeviceDataToVPD-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_WriteDeviceDataToVPD = 'PASSED'
        name_test.append('FFTStart.WriteDeviceDataToVPD')
        result.append([result_WriteDeviceDataToVPD,result_WriteDeviceDataToVPD])
        # print('WriteDeviceDataToVPD: '+result_WriteDeviceDataToVPD)
    except:
        name_test.append('FFTStart.WriteDeviceDataToVPD')
        result.append([result_WriteDeviceDataToVPD,notest])

    # FFT.FFTStart.UpdateVPD
    UpdateVPD = glob.glob(f'{data}\\tests\\FFT.FFTStart.UpdateVPD-*')
    result_UpdateVPD = 'FAILED'
    for up in UpdateVPD:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\UpdateVPD-metadata.txt')
    try:
        with open('result\\UpdateVPD-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_UpdateVPD = 'PASSED'
        name_test.append('FFTStart.UpdateVPD')
        result.append([result_UpdateVPD,result_UpdateVPD])    
        # print('UpdateVPD: '+result_UpdateVPD)
    except:
        name_test.append('FFTStart.UpdateVPD')
        result.append([result_UpdateVPD,notest]) 

    # FFT.FFTStart.UpdateFirmware.UpdateFirmware
    UpdateFirmware = glob.glob(f'{data}\\tests\\FFT.FFTStart.UpdateFirmware.UpdateFirmware-*')
    result_UpdateFirmware = 'FAILED'
    for up in UpdateFirmware:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\UpdateFirmware-metadata.txt')
    try:
        with open('result\\UpdateFirmware-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_UpdateFirmware = 'PASSED'
        name_test.append('FFTStart.UpdateFirmware.UpdateFirmware')  
        result.append([result_UpdateFirmware,result_UpdateFirmware])   
        # print('UpdateFirmware: '+result_UpdateFirmware)
    except:
        name_test.append('FFTStart.UpdateFirmware.UpdateFirmware')  
        result.append([result_UpdateFirmware,notest]) 

    # FFT.FFTStart.UpdateFirmware.Barrier
    UpdateBarrier = glob.glob(f'{data}\\tests\\FFT.FFTStart.UpdateFirmware.Barrier-*')
    result_UpdateBarrier = 'FAILED'
    for up in UpdateBarrier:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\UpdateBarrier-metadata.txt')
    try:
        with open('result\\UpdateBarrier-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_UpdateBarrier = 'PASSED'
        name_test.append('FFTStart.UpdateFirmware.Barrier')  
        result.append([result_UpdateBarrier,result_UpdateBarrier]) 
        #print('UpdateBarrier: '+result_UpdateBarrier)
    except:
        name_test.append('FFTStart.UpdateFirmware.Barrier')  
        result.append([result_UpdateBarrier,notest]) 

    # FFT.FFTStart.UpdateFirmware.RebootStep
    RebootStep = glob.glob(f'{data}\\tests\\FFT.FFTStart.UpdateFirmware.RebootStep-*')
    result_RebootStep = 'FAILED'
    for up in RebootStep:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RebootStep-metadata.txt')
    try:
        with open('result\\RebootStep-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RebootStep = 'PASSED'
        name_test.append('FFTStart.UpdateFirmware.RebootStep')
        result.append([result_RebootStep,result_RebootStep]) 
        # print('RebootStep: '+result_RebootStep)
    except:
        name_test.append('FFTStart.UpdateFirmware.RebootStep')
        result.append([result_RebootStep,notest]) 

    # FFT.FFTStart.WriteHWID
    WriteHWID = glob.glob(f'{data}\\tests\\FFT.FFTStart.WriteHWID-*')
    result_WriteHWID = 'FAILED'
    for up in WriteHWID:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\WriteHWID-metadata.txt')
    try:
        with open('result\\WriteHWID-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_WriteHWID = 'PASSED'
        name_test.append('FFTStart.WriteHWID')
        result.append([result_WriteHWID,result_WriteHWID])    
        # print('WriteHWID: '+result_WriteHWID)
    except:
        name_test.append('FFTStart.WriteHWID')
        result.append([result_WriteHWID,notest])

    # FFT.FFTStart.ModelSKU
    ModelSKU = glob.glob(f'{data}\\tests\\FFT.FFTStart.ModelSKU-*')
    result_ModelSKU = 'FAILED'
    for up in ModelSKU:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\ModelSKU-metadata.txt')
    try:
        with open('result\\ModelSKU-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_ModelSKU = 'PASSED'
        name_test.append('FFTStart.ModelSKU')
        result.append([result_ModelSKU,result_ModelSKU])
        # print('ModelSKU: '+result_ModelSKU)
    except:
        name_test.append('FFTStart.ModelSKU')
        result.append([result_ModelSKU,notest])

    # FFT.Barrier
    Barrier = glob.glob(f'{data}\\tests\\FFT.Barrier-*')
    result_Barrier = 'FAILED'
    for up in Barrier:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\Barrier-metadata.txt')
    try:
        with open('result\\Barrier-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_Barrier = 'PASSED'
        name_test.append('Barrier')
        result.append([result_Barrier,result_Barrier])    
        # print('Barrier: '+result_Barrier)
    except:
        name_test.append('Barrier')
        result.append([result_Barrier,notest]) 

    # FFT.Bluetooth
    Bluetooth = glob.glob(f'{data}\\tests\\FFT.Bluetooth-*')
    result_Bluetooth = 'FAILED'
    for up in Bluetooth:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\Bluetooth-metadata.txt')
    try:
        with open('result\\Bluetooth-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_Bluetooth = 'PASSED'
        name_test.append('Bluetooth')
        result.append([result_Bluetooth,result_Bluetooth])        
        # print('Bluetooth: '+result_Bluetooth)
    except:
        name_test.append('Bluetooth')
        result.append([result_Bluetooth,notest])

    # FFT.CoralWifi
    CoralWifi = glob.glob(f'{data}\\tests\\FFT.CoralWifi-*')
    result_CoralWifi = 'FAILED'
    for up in CoralWifi:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\CoralWifi-metadata.txt')
    try:
        with open('result\\CoralWifi-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_CoralWifi = 'PASSED'
        name_test.append('CoralWifi')
        result.append([result_CoralWifi,result_CoralWifi])      
        # print('CoralWifi: '+result_CoralWifi)
    except:
        name_test.append('CoralWifi')
        result.append([result_CoralWifi,notest])

    # FFT.DisplayPoint
    DisplayPoint = glob.glob(f'{data}\\tests\\FFT.DisplayPoint-*')
    result_DisplayPoint = 'FAILED'
    for up in DisplayPoint:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\DisplayPoint-metadata.txt')
    try:
        with open('result\\DisplayPoint-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_DisplayPoint = 'PASSED'
        name_test.append('DisplayPoint')
        result.append([result_DisplayPoint,result_DisplayPoint])       
        # print('DisplayPoint: '+result_DisplayPoint)
    except:
        name_test.append('DisplayPoint')
        result.append([result_DisplayPoint,notest]) 

    # FFT.Display
    Display = glob.glob(f'{data}\\tests\\FFT.Display-*')
    result_Display = 'FAILED'
    for up in Display:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\Display-metadata.txt')
    try:
        with open('result\\Display-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_Display = 'PASSED'
        name_test.append('Display')
        result.append([result_Display,result_Display])      
        # print('Display: '+result_Display)
    except:
        name_test.append('Display')
        result.append([result_Display,notest])

    # FFT.CoralCamera0
    CoralCamera0 = glob.glob(f'{data}\\tests\\FFT.CoralCamera0-*')
    result_CoralCamera0 = 'FAILED'
    for up in CoralCamera0:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\CoralCamera0-metadata.txt')
    try:
        with open('result\\CoralCamera0-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_CoralCamera0 = 'PASSED'
        name_test.append('CoralCamera0')
        result.append([result_CoralCamera0,result_CoralCamera0])      
        # print('CoralCamera0: '+result_CoralCamera0)
    except:
        name_test.append('CoralCamera0')
        result.append([result_CoralCamera0,notest])

    # FFT.SDPerformance
    SDPerformance = glob.glob(f'{data}\\tests\\FFT.SDPerformance-*')
    result_SDPerformance = 'FAILED'
    for up in SDPerformance:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\SDPerformance-metadata.txt')
    try:
        with open('result\\SDPerformance-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_SDPerformance = 'PASSED'
        name_test.append('SDPerformance')
        result.append([result_SDPerformance,result_SDPerformance])     
        # print('SDPerformance: '+result_SDPerformance)
    except:
        name_test.append('SDPerformance')
        result.append([result_SDPerformance,notest])

    # FFT.USBTypeAManualLeft.USBPerformance
    TypeALeftUSBPerformance = glob.glob(f'{data}\\tests\\FFT.USBTypeAManualLeft.USBPerformance-*')
    result_TypeALeftUSBPerformance = 'FAILED'
    for up in TypeALeftUSBPerformance:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\TypeALeftUSBPerformance-metadata.txt')
    try:
        with open('result\\TypeALeftUSBPerformance-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_TypeALeftUSBPerformance = 'PASSED'
        name_test.append('USBTypeAManualLeft.USBPerformance')
        result.append([result_TypeALeftUSBPerformance,result_TypeALeftUSBPerformance])      
        # print('TypeALeftUSBPerformance: '+result_TypeALeftUSBPerformance)
    except:
        name_test.append('USBTypeAManualLeft.USBPerformance')
        result.append([result_TypeALeftUSBPerformance,notest]) 

    # FFT.USBTypeAManualLeft.USBPerformance_2
    TypeALeftUSBPerformance_2 = glob.glob(f'{data}\\tests\\FFT.USBTypeAManualLeft.USBPerformance_2-*')
    result_TypeALeftUSBPerformance_2 = 'FAILED'
    for up in TypeALeftUSBPerformance_2:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\TypeALeftUSBPerformance_2-metadata.txt')
    try:
        with open('result\\TypeALeftUSBPerformance_2-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_TypeALeftUSBPerformance_2 = 'PASSED'
        name_test.append('USBTypeAManualLeft.USBPerformance_2')
        result.append([result_TypeALeftUSBPerformance_2,result_TypeALeftUSBPerformance_2])     
        # print('TypeALeftUSBPerformance_2: '+result_TypeALeftUSBPerformance_2)
    except:
        name_test.append('USBTypeAManualLeft.USBPerformance_2')
        result.append([result_TypeALeftUSBPerformance_2,notest])

    # FFT.USBTypeAManualRight.USBPerformance
    TypeARightUSBPerformance = glob.glob(f'{data}\\tests\\FFT.USBTypeAManualRight.USBPerformance-*')
    result_TypeARightUSBPerformance = 'FAILED'
    for up in TypeARightUSBPerformance:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\TypeARightUSBPerformance-metadata.txt')
    try:
        with open('result\\TypeARightUSBPerformance-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_TypeARightUSBPerformance = 'PASSED'
        name_test.append('USBTypeAManualRight.USBPerformance')
        result.append([result_TypeARightUSBPerformance,result_TypeARightUSBPerformance])     
        # print('TypeARightUSBPerformance: '+result_TypeARightUSBPerformance)
    except:
        name_test.append('USBTypeAManualRight.USBPerformance')
        result.append([result_TypeARightUSBPerformance,notest])

    # FFT.USBTypeAManualRight.USBPerformance_2
    TypeARightUSBPerformance_2 = glob.glob(f'{data}\\tests\\FFT.USBTypeAManualRight.USBPerformance_2-*')
    result_TypeARightUSBPerformance_2 = 'FAILED'
    for up in TypeARightUSBPerformance_2:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\TypeARightUSBPerformance_2-metadata.txt')
    try:
        with open('result\\TypeARightUSBPerformance_2-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_TypeARightUSBPerformance_2 = 'PASSED'
        name_test.append('USBTypeAManualRight.USBPerformance_2')
        result.append([result_TypeARightUSBPerformance_2,result_TypeARightUSBPerformance_2])     
        # print('TypeARightUSBPerformance_2: '+result_TypeARightUSBPerformance_2)
    except:
        name_test.append('USBTypeAManualRight.USBPerformance_2')
        result.append([result_TypeARightUSBPerformance_2,notest])

    # FFT.USBTypeCManualLeft.USBPerformance
    TypeCLeftUSBPerformance = glob.glob(f'{data}\\tests\\FFT.USBTypeCManualLeft.USBPerformance-*')
    result_TypeCLeftUSBPerformance = 'FAILED'
    for up in TypeCLeftUSBPerformance:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\TypeCLeftUSBPerformance-metadata.txt')
    try:
        with open('result\\TypeCLeftUSBPerformance-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_TypeCLeftUSBPerformance = 'PASSED'
        name_test.append('FFT.USBTypeCManualLeft.USBPerformance')
        result.append([result_TypeCLeftUSBPerformance,result_TypeCLeftUSBPerformance])   
        # print('TypeCLeftUSBPerformance: '+result_TypeCLeftUSBPerformance)
    except:
        name_test.append('FFT.USBTypeCManualLeft.USBPerformance')
        result.append([result_TypeCLeftUSBPerformance,notest]) 

    # FFT.USBTypeCManualLeft.USBPerformance_2
    TypeCLeftUSBPerformance_2 = glob.glob(f'{data}\\tests\\FFT.USBTypeCManualLeft.USBPerformance_2-*')
    result_TypeCLeftUSBPerformance_2 = 'FAILED'
    for up in TypeCLeftUSBPerformance_2:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\TypeCLeftUSBPerformance_2-metadata.txt')
    try:
        with open('result\\TypeCLeftUSBPerformance_2-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_TypeCLeftUSBPerformance_2 = 'PASSED'
        name_test.append('FFT.USBTypeCManualLeft.USBPerformance_2')
        result.append([result_TypeCLeftUSBPerformance_2,result_TypeCLeftUSBPerformance_2])      
        # print('TypeCLeftUSBPerformance_2: '+result_TypeCLeftUSBPerformance_2)
    except:
        name_test.append('FFT.USBTypeCManualLeft.USBPerformance_2')
        result.append([result_TypeCLeftUSBPerformance_2,notest])

    # FFT.USBTypeCManualLeft.USBPerformance_3
    TypeCLeftUSBPerformance_3 = glob.glob(f'{data}\\tests\\FFT.USBTypeCManualLeft.USBPerformance_3-*')
    result_TypeCLeftUSBPerformance_3 = 'FAILED'
    for up in TypeCLeftUSBPerformance_3:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\TypeCLeftUSBPerformance_3-metadata.txt')
    try:
        with open('result\\TypeCLeftUSBPerformance_3-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_TypeCLeftUSBPerformance_3 = 'PASSED'
        name_test.append('USBTypeCManualLeft.USBPerformance_3') 
        result.append([result_TypeCLeftUSBPerformance_3,result_TypeCLeftUSBPerformance_3])   
        # print('TypeCLeftUSBPerformance_3: '+result_TypeCLeftUSBPerformance_3)
    except:
        name_test.append('USBTypeCManualLeft.USBPerformance_3') 
        result.append([result_TypeCLeftUSBPerformance_3,notest])

    # FFT.USBTypeCManualLeft.ExternalDisplay
    LeftExternalDisplay = glob.glob(f'{data}\\tests\\FFT.USBTypeCManualLeft.ExternalDisplay-*')
    result_LeftExternalDisplay = 'FAILED'
    for up in LeftExternalDisplay:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\LeftExternalDisplay-metadata.txt')
    try:
        with open('result\\LeftExternalDisplay-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_LeftExternalDisplay = 'PASSED'
        name_test.append('USBTypeCManualLeft.ExternalDisplay')
        result.append([result_LeftExternalDisplay,result_LeftExternalDisplay])    
        # print('LeftExternalDisplay: '+result_LeftExternalDisplay)
    except:
        name_test.append('USBTypeCManualLeft.ExternalDisplay')
        result.append([result_LeftExternalDisplay,notest])

    # FFT.USBTypeCManualLeft.Barrier
    LeftBarrier = glob.glob(f'{data}\\tests\\FFT.USBTypeCManualLeft.Barrier-*')
    result_LeftBarrier = 'FAILED'
    for up in LeftBarrier:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\LeftBarrier-metadata.txt')
    try:
        with open('result\\LeftBarrier-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_LeftBarrier = 'PASSED'
        name_test.append('USBTypeCManualLeft.Barrier')
        result.append([result_LeftBarrier,result_LeftBarrier])      
        # print('LeftBarrier: '+result_LeftBarrier)
    except:
        name_test.append('USBTypeCManualLeft.Barrier')
        result.append([result_LeftBarrier,notest])

    # FFT.Keyboard
    Keyboard = glob.glob(f'{data}\\tests\\FFT.Keyboard-*')
    result_Keyboard = 'FAILED'
    for up in Keyboard:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\Keyboard-metadata.txt')
    try:
        with open('result\\Keyboard-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_Keyboard = 'PASSED'
        name_test.append('Keyboard')
        result.append([result_Keyboard,result_Keyboard])      
        # print('Keyboard: '+result_Keyboard)
    except:
        name_test.append('Keyboard')
        result.append([result_Keyboard,notest])

    # FFT.LidSwitch
    LidSwitch = glob.glob(f'{data}\\tests\\FFT.LidSwitch-*')
    result_LidSwitch = 'FAILED'
    for up in LidSwitch:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\LidSwitch-metadata.txt')
    try:
        with open('result\\LidSwitch-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_LidSwitch = 'PASSED'
        name_test.append('LidSwitch')
        result.append([result_LidSwitch,result_LidSwitch])   
        # print('LidSwitch: '+result_LidSwitch)
    except:
        name_test.append('LidSwitch')
        result.append([result_LidSwitch,notest]) 

    # FFT.BatteryLED
    BatteryLED = glob.glob(f'{data}\\tests\\FFT.BatteryLED-*')
    result_BatteryLED = 'FAILED'
    for up in BatteryLED:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\BatteryLED-metadata.txt')
    try:
        with open('result\\BatteryLED-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_BatteryLED = 'PASSED'
        name_test.append('BatteryLED')
        result.append([result_BatteryLED,result_BatteryLED])   
        #print('BatteryLED: '+result_BatteryLED)
    except:
        name_test.append('BatteryLED')
        result.append([result_BatteryLED,notest])   

    # FFT.USBTypeCManualRight.USBPerformance
    TypeCRightUSBPerformance = glob.glob(f'{data}\\tests\\FFT.USBTypeCManualRight.USBPerformance-*')
    result_TypeCRightUSBPerformance = 'FAILED'
    for up in TypeCRightUSBPerformance:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\TypeCRightUSBPerformance-metadata.txt')
    try:
        with open('result\\TypeCRightUSBPerformance-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_TypeCRightUSBPerformance = 'PASSED'
        name_test.append('USBTypeCManualRight.USBPerformance')
        result.append([result_TypeCRightUSBPerformance,result_TypeCRightUSBPerformance])    
        # print('TypeCRightUSBPerformance: '+result_TypeCRightUSBPerformance)
    except:
        name_test.append('USBTypeCManualRight.USBPerformance')
        result.append([result_TypeCRightUSBPerformance,notest]) 

    # FFT.USBTypeCManualRight.USBPerformance_2
    TypeCRightUSBPerformance_2 = glob.glob(f'{data}\\tests\\FFT.USBTypeCManualRight.USBPerformance_2-*')
    result_TypeCRightUSBPerformance_2 = 'FAILED'
    for up in TypeCRightUSBPerformance_2:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\TypeCRightUSBPerformance_2-metadata.txt')
    try:
        with open('result\\TypeCRightUSBPerformance_2-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_TypeCRightUSBPerformance_2 = 'PASSED'
        name_test.append('USBTypeCManualRight.USBPerformance_2')
        result.append([result_TypeCRightUSBPerformance_2,result_TypeCRightUSBPerformance_2])      
        # print('TypeCRightUSBPerformance_2: '+result_TypeCRightUSBPerformance_2)
    except:
        name_test.append('USBTypeCManualRight.USBPerformance_2')
        result.append([result_TypeCRightUSBPerformance_2,notest])

    # FFT.USBTypeCManualRight.USBPerformance_3
    TypeCRightUSBPerformance_3 = glob.glob(f'{data}\\tests\\FFT.USBTypeCManualRight.USBPerformance_3-*')
    result_TypeCRightUSBPerformance_3 = 'FAILED'
    for up in TypeCRightUSBPerformance_3:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\TypeCRightUSBPerformance_3-metadata.txt')
    try:
        with open('result\\TypeCRightUSBPerformance_3-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_TypeCRightUSBPerformance_3 = 'PASSED'
        name_test.append('USBTypeCManualRight.USBPerformance_3')
        result.append([result_TypeCRightUSBPerformance_3,result_TypeCRightUSBPerformance_3])       
        # print('TypeCRightUSBPerformance_3: '+result_TypeCRightUSBPerformance_3)
    except:
        name_test.append('USBTypeCManualRight.USBPerformance_3')
        result.append([result_TypeCRightUSBPerformance_3,notest])

    # FFT.USBTypeCManualRight.ExternalDisplay
    RightExternalDisplay = glob.glob(f'{data}\\tests\\FFT.USBTypeCManualRight.ExternalDisplay-*')
    result_RightExternalDisplay = 'FAILED'
    for up in RightExternalDisplay:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RightExternalDisplay-metadata.txt')
    try:
        with open('result\\RightExternalDisplay-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RightExternalDisplay = 'PASSED'
        name_test.append('USBTypeCManualRight.ExternalDisplay')
        result.append([result_RightExternalDisplay,result_RightExternalDisplay])   
        # print('RightExternalDisplay: '+result_RightExternalDisplay)
    except:
        name_test.append('USBTypeCManualRight.ExternalDisplay')
        result.append([result_RightExternalDisplay,notest]) 

    # FFT.USBTypeCManualRight.Barrier
    RightBarrier = glob.glob(f'{data}\\tests\\FFT.USBTypeCManualRight.Barrier-*')
    result_RightBarrier = 'FAILED'
    for up in RightBarrier:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RightBarrier-metadata.txt')
    try:
        with open('result\\RightBarrier-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RightBarrier = 'PASSED'
        name_test.append('USBTypeCManualRight.Barrier')
        result.append([result_RightBarrier,result_RightBarrier])     
        # print('RightBarrier: '+result_RightBarrier)
    except:
        name_test.append('USBTypeCManualRight.Barrier')
        result.append([result_RightBarrier,notest])

    # FFT.HWButton.Button_3
    Button_3 = glob.glob(f'{data}\\tests\\FFT.HWButton.Button_3-*')
    result_Button_3 = 'FAILED'
    for up in Button_3:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\Button_3-metadata.txt')
    try:
        with open('result\\Button_3-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_Button_3 = 'PASSED'
        name_test.append('HWButton.Button_3')
        result.append([result_Button_3,result_Button_3])      
        # print('Button_3: '+result_Button_3)
    except:
        name_test.append('HWButton.Button_3')
        result.append([result_Button_3,notest]) 

    # FFT.AudioRecordTest
    AudioRecordTest = glob.glob(f'{data}\\tests\\FFT.AudioRecordTest-*')
    result_AudioRecordTest = 'FAILED'
    for up in AudioRecordTest:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\AudioRecordTest-metadata.txt')
    try:
        with open('result\\AudioRecordTest-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_AudioRecordTest = 'PASSED'
        name_test.append('AudioRecordTest')
        result.append([result_AudioRecordTest,result_AudioRecordTest])       
        # print('AudioRecordTest: '+result_AudioRecordTest)
    except:
        name_test.append('AudioRecordTest')
        result.append([result_AudioRecordTest,notest])

    # FFT.SpeakerDMic
    SpeakerDMic = glob.glob(f'{data}\\tests\\FFT.SpeakerDMic-*')
    result_SpeakerDMic = 'FAILED'
    for up in SpeakerDMic:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\SpeakerDMic-metadata.txt')
    try:
        with open('result\\SpeakerDMic-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_SpeakerDMic = 'PASSED'
        name_test.append('SpeakerDMic')
        result.append([result_SpeakerDMic,result_SpeakerDMic])      
        # print('SpeakerDMic: '+result_SpeakerDMic)
    except:
        name_test.append('SpeakerDMic')
        result.append([result_SpeakerDMic,notest])

    # FFT.Touchpad
    Touchpad = glob.glob(f'{data}\\tests\\FFT.Touchpad-*')
    result_Touchpad = 'FAILED'
    for up in Touchpad:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\Touchpad-metadata.txt')
    try:
        with open('result\\Touchpad-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_Touchpad = 'PASSED'
        name_test.append('Touchpad')
        result.append([result_Touchpad,result_Touchpad])     
        # print('Touchpad: '+result_Touchpad)
    except:
        name_test.append('Touchpad')
        result.append([result_Touchpad,notest])

    # FFT.BatterySysfs
    BatterySysfs = glob.glob(f'{data}\\tests\\FFT.BatterySysfs-*')
    result_BatterySysfs = 'FAILED'
    for up in BatterySysfs:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\BatterySysfs-metadata.txt')
    try:
        with open('result\\BatterySysfs-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_BatterySysfs = 'PASSED'
        name_test.append('BatterySysfs')
        result.append([result_BatterySysfs,result_BatterySysfs])    
        # print('BatterySysfs: '+result_BatterySysfs)
    except:
        name_test.append('BatterySysfs')
        result.append([result_BatterySysfs,notest])

    # FFT.Battery
    Battery = glob.glob(f'{data}\\tests\\FFT.Battery-*')
    result_Battery = 'FAILED'
    for up in Battery:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\Battery-metadata.txt')
    try:
        with open('result\\Battery-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_Battery = 'PASSED'
        name_test.append('Battery')
        result.append([result_Battery,result_Battery])      
        # print('Battery: '+result_Battery)
    except:
        name_test.append('Battery')
        result.append([result_Battery,notest])

    # FFT.ChargeDischargeCurrentGroup.ChargeDischargeCurrent
    ChargeDischargeCurrent = glob.glob(f'{data}\\tests\\FFT.ChargeDischargeCurrentGroup.ChargeDischargeCurrent-*')
    result_ChargeDischargeCurrent = 'FAILED'
    for up in ChargeDischargeCurrent:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\ChargeDischargeCurrent-metadata.txt')
    try:
        with open('result\\ChargeDischargeCurrent-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_ChargeDischargeCurrent = 'PASSED'
        name_test.append('ChargeDischargeCurrentGroup.ChargeDischargeCurrent')
        result.append([result_ChargeDischargeCurrent,result_ChargeDischargeCurrent])      
        # print('ChargeDischargeCurrent: '+result_ChargeDischargeCurrent)
    except:
        name_test.append('ChargeDischargeCurrentGroup.ChargeDischargeCurrent')
        result.append([result_ChargeDischargeCurrent,notest])

    # FFT.ChargeDischargeCurrentGroup.ChargeDischargeCurrent_2
    ChargeDischargeCurrent_2 = glob.glob(f'{data}\\tests\\FFT.ChargeDischargeCurrentGroup.ChargeDischargeCurrent_2-*')
    result_ChargeDischargeCurrent_2 = 'FAILED'
    for up in ChargeDischargeCurrent_2:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\ChargeDischargeCurrent_2-metadata.txt')
    try:
        with open('result\\ChargeDischargeCurrent_2-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_ChargeDischargeCurrent_2 = 'PASSED'
        name_test.append('ChargeDischargeCurrentGroup.ChargeDischargeCurrent_2')
        result.append([result_ChargeDischargeCurrent_2,result_ChargeDischargeCurrent_2])    
        # print('ChargeDischargeCurrent_2: '+result_ChargeDischargeCurrent_2)
    except:
        name_test.append('ChargeDischargeCurrentGroup.ChargeDischargeCurrent_2')
        result.append([result_ChargeDischargeCurrent_2,notest])

    # FFT.ThermalSensors
    ThermalSensors = glob.glob(f'{data}\\tests\\FFT.ThermalSensors-*')
    result_ThermalSensors = 'FAILED'
    for up in ThermalSensors:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\ThermalSensors-metadata.txt')
    try:
        with open('result\\ThermalSensors-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_ThermalSensors = 'PASSED'
        name_test.append('ThermalSensors')
        result.append([result_ThermalSensors,result_ThermalSensors])       
        # print('ThermalSensors: '+result_ThermalSensors)
    except:
        name_test.append('ThermalSensors')
        result.append([result_ThermalSensors,notest])

    # FFT.MRCCache.CreateCache
    CreateCache = glob.glob(f'{data}\\tests\\FFT.MRCCache.CreateCache-*')
    result_CreateCache = 'FAILED'
    for up in CreateCache:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\CreateCache-metadata.txt')
    try:
        with open('result\\CreateCache-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_CreateCache = 'PASSED'
        name_test.append('MRCCache.CreateCache')
        result.append([result_CreateCache,result_CreateCache])      
        # print('CreateCache: '+result_CreateCache)
    except:
        name_test.append('MRCCache.CreateCache')
        result.append([result_CreateCache,notest])

    # FFT.MRCCache.RebootStep
    RebootStep = glob.glob(f'{data}\\tests\\FFT.MRCCache.RebootStep-*')
    result_RebootStep = 'FAILED'
    for up in RebootStep:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RebootStep-metadata.txt')
    try:
        with open('result\\RebootStep-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RebootStep = 'PASSED'
        name_test.append('MRCCache.RebootStep')
        result.append([result_RebootStep,result_RebootStep])       
        # print('RebootStep: '+result_RebootStep)
    except:
        name_test.append('MRCCache.RebootStep')
        result.append([result_RebootStep,notest])

    # FFT.MRCCache.VerifyCache
    VerifyCache = glob.glob(f'{data}\\tests\\FFT.MRCCache.VerifyCache-*')
    result_VerifyCache = 'FAILED'
    for up in VerifyCache:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\VerifyCache-metadata.txt')
    try:
        with open('result\\VerifyCache-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_VerifyCache = 'PASSED'
        name_test.append('MRCCache.VerifyCache')
        result.append([result_VerifyCache,result_VerifyCache])     
        # print('VerifyCache: '+result_VerifyCache)
    except:
        name_test.append('MRCCache.VerifyCache')
        result.append([result_VerifyCache,notest]) 

    # FFT.Barrier_2
    Barrier_2 = glob.glob(f'{data}\\tests\\FFT.Barrier_2-*')
    result_Barrier_2 = 'FAILED'
    for up in Barrier_2:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\Barrier_2-metadata.txt')
    try:
        with open('result\\Barrier_2-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_Barrier_2 = 'PASSED'
        name_test.append('Barrier_2')
        result.append([result_Barrier_2,result_Barrier_2])      
        # print('Barrier_2: '+result_Barrier_2)
    except:
        name_test.append('Barrier_2')
        result.append([result_Barrier_2,notest])

    ###############################################################################
    # FFT.Finish
    Finish = glob.glob(f'{data}\\tests\\FFT.Finish-*')
    result_Finish = 'FAILED'
    for up in Finish:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\Finish-metadata.txt')
    try:
        with open('result\\Finish-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_Finish = 'PASSED'    
        # print('Finish: '+result_Finish)
    except:
        result_Finish = 'FAILED'
    ################################################################################

    # RunInFAT.Start-
    RunInFATStart = glob.glob(f'{data}\\tests\\RunInFAT.Start-*')
    result_RunInFATStart = 'FAILED'
    for up in RunInFATStart:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATStart-metadata.txt')
    try:
        with open('result\\RunInFATStart-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATStart = 'PASSED'
        name_test.append('RunInFAT.Start')
        result.append([result_RunInFATStart,result_RunInFATStart])      
        # print('RunInFATStart: '+result_RunInFATStart)
    except:
        name_test.append('RunInFATStart')
        result.append([result_RunInFATStart,notest])

    # RunInFAT.TouchpadProbe-
    RunInFATTouchpadProbe = glob.glob(f'{data}\\tests\\RunInFAT.TouchpadProbe-*')
    result_RunInFATTouchpadProbe = 'FAILED'
    for up in RunInFATTouchpadProbe:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATTouchpadProbe-metadata.txt')
    try:
        with open('result\\RunInFATTouchpadProbe-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATTouchpadProbe = 'PASSED'
        name_test.append('RunInFAT.TouchpadProbe')
        result.append([result_RunInFATTouchpadProbe,result_RunInFATTouchpadProbe])      
        # print('RunInFATTouchpadProbe: '+result_RunInFATTouchpadProbe)
    except:
        name_test.append('RunInFAT.TouchpadProbe')
        result.append([result_RunInFATTouchpadProbe,notest])

    # RunInFAT.BluetoothProbe-
    RunInFATBluetoothProbe = glob.glob(f'{data}\\tests\\RunInFAT.BluetoothProbe-*')
    result_RunInFATBluetoothProbe = 'FAILED'
    for up in RunInFATBluetoothProbe:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATBluetoothProbe-metadata.txt')
    try:
        with open('result\\RunInFATBluetoothProbe-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATBluetoothProbe = 'PASSED'
        name_test.append('RunInFAT.BluetoothProbe')
        result.append([result_RunInFATBluetoothProbe,result_RunInFATBluetoothProbe])      
        # print('RunInFATBluetoothProbe: '+result_RunInFATBluetoothProbe)
    except:
        name_test.append('RunInFAT.BluetoothProbe')
        result.append([result_RunInFATBluetoothProbe,notest])

    # RunInFAT.PartitionTable-
    RunInFATPartitionTable = glob.glob(f'{data}\\tests\\RunInFAT.PartitionTable-*')
    result_RunInFATPartitionTable = 'FAILED'
    for up in RunInFATPartitionTable:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATPartitionTable-metadata.txt')
    try:
        with open('result\\RunInFATPartitionTable-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATPartitionTable = 'PASSED'
        name_test.append('RunInFAT.PartitionTable')
        result.append([result_RunInFATPartitionTable,result_RunInFATPartitionTable])      
        # print('RunInFATPartitionTable: '+result_RunInFATPartitionTable)
    except:
        name_test.append('RunInFAT.PartitionTable')
        result.append([result_RunInFATPartitionTable,notest])

    # RunInFAT.VerifyRootPartition-
    RunInFATVerifyRootPartition = glob.glob(f'{data}\\tests\\RunInFAT.VerifyRootPartition-*')
    result_RunInFATVerifyRootPartition = 'FAILED'
    for up in RunInFATVerifyRootPartition:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATVerifyRootPartition-metadata.txt')
    try:
        with open('result\\RunInFATVerifyRootPartition-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATVerifyRootPartition = 'PASSED'
        name_test.append('RunInFAT.VerifyRootPartition')
        result.append([result_RunInFATVerifyRootPartition,result_RunInFATVerifyRootPartition])      
        # print('RunInFATVerifyRootPartition: '+result_RunInFATVerifyRootPartition)
    except:
        name_test.append('RunInFAT.VerifyRootPartition')
        result.append([result_RunInFATVerifyRootPartition,notest])

    # RunInFAT.BadBlocks-
    RunInFATBadBlocks = glob.glob(f'{data}\\tests\\RunInFAT.BadBlocks-*')
    result_RunInFATBadBlocks = 'FAILED'
    for up in RunInFATBadBlocks:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATBadBlocks-metadata.txt')
    try:
        with open('result\\RunInFATBadBlocks-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATBadBlocks = 'PASSED'
        name_test.append('RunInFAT.BadBlocks')
        result.append([result_RunInFATBadBlocks,result_RunInFATBadBlocks])      
        # print('RunInFATBadBlocks: '+result_RunInFATBadBlocks)
    except:
        name_test.append('RunInFAT.BadBlocks')
        result.append([result_RunInFATBadBlocks,notest])

    # RunInFAT.Barrier_2-
    RunInFATBarrier_2 = glob.glob(f'{data}\\tests\\RunInFAT.Barrier_2-*')
    result_RunInFATBarrier_2 = 'FAILED'
    for up in RunInFATBarrier_2:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATBarrier_2-metadata.txt')
    try:
        with open('result\\RunInFATBarrier_2-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATBarrier_2 = 'PASSED'
        name_test.append('RunInFAT.Barrier_2')
        result.append([result_RunInFATBarrier_2,result_RunInFATBarrier_2])      
        # print('RunInFATBarrier_2: '+result_RunInFATBarrier_2)
    except:
        name_test.append('RunInFAT.Barrier_2')
        result.append([result_RunInFATBarrier_2,notest])

    # RunInFAT.RebootStep-
    RunInFATRebootStep = glob.glob(f'{data}\\tests\\RunInFAT.RebootStep-*')
    result_RunInFATRebootStep = 'FAILED'
    for up in RunInFATRebootStep:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRebootStep-metadata.txt')
    try:
        with open('result\\RunInFATRebootStep-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRebootStep = 'PASSED'
        name_test.append('RunInFAT.RebootStep')
        result.append([result_RunInFATRebootStep,result_RunInFATRebootStep])      
        # print('RunInFATRebootStep: '+result_RunInFATRebootStep)
    except:
        name_test.append('RunInFAT.RebootStep')
        result.append([result_RunInFATRebootStep,notest])

    # RunInFAT.RunInStressGroup.WebGLAquarium-
    RunInFATRunInStressGroupWebGLAquarium = glob.glob(f'{data}\\tests\\RunInFAT.RunInStressGroup.WebGLAquarium-*')
    result_RunInFATRunInStressGroupWebGLAquarium = 'FAILED'
    for up in RunInFATRunInStressGroupWebGLAquarium:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRunInStressGroupWebGLAquarium-metadata.txt')
    try:
        with open('result\\RunInFATRunInStressGroupWebGLAquarium-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRunInStressGroupWebGLAquarium = 'PASSED'
        name_test.append('RunInFAT.RunInStressGroup.WebGLAquarium')
        result.append([result_RunInFATRunInStressGroupWebGLAquarium,result_RunInFATRunInStressGroupWebGLAquarium])      
        # print('RunInFATRunInStressGroupWebGLAquarium: '+result_RunInFATRunInStressGroupWebGLAquarium)
    except:
        name_test.append('RunInFAT.RunInStressGroup.WebGLAquarium')
        result.append([result_RunInFATRunInStressGroupWebGLAquarium,notest])

    # RunInFAT.RunInStressGroup.URandom-
    RunInFATRunInStressGroupURandom = glob.glob(f'{data}\\tests\\RunInFAT.RunInStressGroup.URandom-*')
    result_RunInFATRunInStressGroupURandom = 'FAILED'
    for up in RunInFATRunInStressGroupURandom:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRunInStressGroupURandom-metadata.txt')
    try:
        with open('result\\RunInFATRunInStressGroupURandom-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRunInStressGroupURandom = 'PASSED'
        name_test.append('RunInFAT.RunInStressGroup.URandom')
        result.append([result_RunInFATRunInStressGroupURandom,result_RunInFATRunInStressGroupURandom])      
        # print('RunInFATRunInStressGroupURandom: '+result_RunInFATRunInStressGroupURandom)
    except:
        name_test.append('RunInFAT.RunInStressGroup.URandom')
        result.append([result_RunInFATRunInStressGroupURandom,notest])

    # RunInFAT.RunInStressGroup.Camera-
    RunInFATRunInStressGroupCamera = glob.glob(f'{data}\\tests\\RunInFAT.RunInStressGroup.Camera-*')
    result_RunInFATRunInStressGroupCamera = 'FAILED'
    for up in RunInFATRunInStressGroupCamera:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRunInStressGroupCamera-metadata.txt')
    try:
        with open('result\\RunInFATRunInStressGroupCamera-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRunInStressGroupCamera = 'PASSED'
        name_test.append('RunInFAT.RunInStressGroup.Camera')
        result.append([result_RunInFATRunInStressGroupCamera,result_RunInFATRunInStressGroupCamera])      
        # print('RunInFATRunInStressGroupCamera: '+result_RunInFATRunInStressGroupCamera)
    except:
        name_test.append('RunInFAT.RunInStressGroup.Camera')
        result.append([result_RunInFATRunInStressGroupCamera,notest])

    # RunInFAT.RunInStressGroup.RunInCountdown-
    RunInFATRunInStressGroupRunInCountdown = glob.glob(f'{data}\\tests\\RunInFAT.RunInStressGroup.RunInCountdown-*')
    result_RunInFATRunInStressGroupRunInCountdown = 'FAILED'
    for up in RunInFATRunInStressGroupRunInCountdown:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRunInStressGroupRunInCountdown-metadata.txt')
    try:
        with open('result\\RunInFATRunInStressGroupRunInCountdown-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRunInStressGroupRunInCountdown = 'PASSED'
        name_test.append('RunInFAT.RunInStressGroup.RunInCountdown')
        result.append([result_RunInFATRunInStressGroupRunInCountdown,result_RunInFATRunInStressGroupRunInCountdown])      
        # print('RunInFATRunInStressGroupRunInCountdown: '+result_RunInFATRunInStressGroupRunInCountdown)
    except:
        name_test.append('RunInFAT.RunInStressGroup.RunInCountdown')
        result.append([result_RunInFATRunInStressGroupRunInCountdown,notest])

    # RunInFAT.RunInStressGroup.StressAppTest-
    RunInFATRunInStressGroupStressAppTest = glob.glob(f'{data}\\tests\\RunInFAT.RunInStressGroup.StressAppTest-*')
    result_RunInFATRunInStressGroupStressAppTest = 'FAILED'
    for up in RunInFATRunInStressGroupStressAppTest:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRunInStressGroupStressAppTest-metadata.txt')
    try:
        with open('result\\RunInFATRunInStressGroupStressAppTest-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRunInStressGroupStressAppTest = 'PASSED'
        name_test.append('RunInFAT.RunInStressGroup.StressAppTest')
        result.append([result_RunInFATRunInStressGroupStressAppTest,result_RunInFATRunInStressGroupStressAppTest])      
        # print('RunInFATRunInStressGroupStressAppTest: '+result_RunInFATRunInStressGroupStressAppTest)
    except:
        name_test.append('RunInFAT.RunInStressGroup.StressAppTest')
        result.append([result_RunInFATRunInStressGroupStressAppTest,notest])

    # RunInFAT.Barrier_3-
    RunInFATBarrier_3 = glob.glob(f'{data}\\tests\\RunInFAT.Barrier_3-*')
    result_RunInFATBarrier_3 = 'FAILED'
    for up in RunInFATBarrier_3:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATBarrier_3-metadata.txt')
    try:
        with open('result\\RunInFATBarrier_3-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATBarrier_3 = 'PASSED'
        name_test.append('RunInFAT.Barrier_3')
        result.append([result_RunInFATBarrier_3,result_RunInFATBarrier_3])      
        # print('RunInFATBarrier_3: '+result_RunInFATBarrier_3)
    except:
        name_test.append('RunInFAT.Barrier_3')
        result.append([result_RunInFATBarrier_3,notest])

    # RunInFAT.RebootStep_2-
    RunInFATRebootStep_2 = glob.glob(f'{data}\\tests\\RunInFAT.RebootStep_2-*')
    result_RunInFATRebootStep_2 = 'FAILED'
    for up in RunInFATRebootStep_2:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRebootStep_2-metadata.txt')
    try:
        with open('result\\RunInFATRebootStep_2-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRebootStep_2 = 'PASSED'
        name_test.append('RunInFAT.RebootStep_2')
        result.append([result_RunInFATRebootStep_2,result_RunInFATRebootStep_2])      
        # print('RunInFATRebootStep_2: '+result_RunInFATRebootStep_2)
    except:
        name_test.append('RunInFAT.RebootStep')
        result.append([result_RunInFATRebootStep,notest])

    # RunInFAT.RunInDozingStress.SuspendResume-
    RunInFATRunInDozingStressSuspendResume = glob.glob(f'{data}\\tests\\RunInFAT.RunInDozingStress.SuspendResume-*')
    result_RunInFATRunInDozingStressSuspendResume = 'FAILED'
    for up in RunInFATRunInDozingStressSuspendResume:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRunInDozingStressSuspendResume-metadata.txt')
    try:
        with open('result\\RunInFATRunInDozingStressSuspendResume-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRunInDozingStressSuspendResume = 'PASSED'
        name_test.append('RunInFAT.RunInDozingStress.SuspendResume')
        result.append([result_RunInFATRunInDozingStressSuspendResume,result_RunInFATRunInDozingStressSuspendResume])      
        # print('RunInFATRunInDozingStressSuspendResume: '+result_RunInFATRunInDozingStressSuspendResume)
    except:
        name_test.append('RunInFAT.RunInDozingStress.SuspendResume')
        result.append([result_RunInFATRunInDozingStressSuspendResume,notest])

    # RunInFAT.RunInDozingStress.RunInCountdown-
    RunInFATRunInDozingStressRunInCountdown = glob.glob(f'{data}\\tests\\RunInFAT.RunInDozingStress.RunInCountdown-*')
    result_RunInFATRunInDozingStressRunInCountdown = 'FAILED'
    for up in RunInFATRunInDozingStressRunInCountdown:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRunInDozingStressRunInCountdown-metadata.txt')
    try:
        with open('result\\RunInFATRunInDozingStressRunInCountdown-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRunInDozingStressRunInCountdown = 'PASSED'
        name_test.append('RunInFAT.RunInDozingStress.RunInCountdown')
        result.append([result_RunInFATRunInDozingStressRunInCountdown,result_RunInFATRunInDozingStressRunInCountdown])      
        # print('RunInFATRunInDozingStressRunInCountdown: '+result_RunInFATRunInDozingStressRunInCountdown)
    except:
        name_test.append('RunInFAT.RunInDozingStress.RunInCountdown')
        result.append([result_RunInFATRunInDozingStressRunInCountdown,notest])

    # RunInFAT.RunInDozingStress.StressAppTest-
    RunInFATRunInDozingStressStressAppTest = glob.glob(f'{data}\\tests\\RunInFAT.RunInDozingStress.StressAppTest-*')
    result_RunInFATRunInDozingStressStressAppTest = 'FAILED'
    for up in RunInFATRunInDozingStressStressAppTest:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRunInDozingStressStressAppTest-metadata.txt')
    try:
        with open('result\\RunInFATRunInDozingStressStressAppTest-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRunInDozingStressStressAppTest = 'PASSED'
        name_test.append('RunInFAT.RunInDozingStress.StressAppTest')
        result.append([result_RunInFATRunInDozingStressStressAppTest,result_RunInFATRunInDozingStressStressAppTest])      
        # print('RunInFATRunInDozingStressStressAppTest: '+result_RunInFATRunInDozingStressStressAppTest)
    except:
        name_test.append('RunInFAT.RunInDozingStress.StressAppTest')
        result.append([result_RunInFATRunInDozingStressStressAppTest,notest])

    # RunInFAT.Barrier_4-
    RunInFATBarrier_4 = glob.glob(f'{data}\\tests\\RunInFAT.Barrier_4-*')
    result_RunInFATBarrier_4 = 'FAILED'
    for up in RunInFATBarrier_4:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATBarrier_4-metadata.txt')
    try:
        with open('result\\RunInFATBarrier_4-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATBarrier_4 = 'PASSED'
        name_test.append('RunInFAT.Barrier_4')
        result.append([result_RunInFATBarrier_4,result_RunInFATBarrier_4])      
        # print('RunInFATBarrier_4: '+result_RunInFATBarrier_4)
    except:
        name_test.append('RunInFAT.Barrier_4')
        result.append([result_RunInFATBarrier_4,notest])

    # RunInFAT.RunInRebootSequence-
    RunInFATRunInRebootSequence = glob.glob(f'{data}\\tests\\RunInFAT.RunInRebootSequence-*')
    result_RunInFATRunInRebootSequence = 'FAILED'
    for up in RunInFATRunInRebootSequence:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRunInRebootSequence-metadata.txt')
    try:
        with open('result\\RunInFATRunInRebootSequence-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRunInRebootSequence = 'PASSED'
        name_test.append('RunInFAT.RunInRebootSequence')
        result.append([result_RunInFATRunInRebootSequence,result_RunInFATRunInRebootSequence])      
        # print('RunInFATRunInRebootSequence: '+result_RunInFATRunInRebootSequence)
    except:
        name_test.append('RunInFAT.RunInRebootSequence')
        result.append([result_RunInFATRunInRebootSequence,notest])

    # RunInFAT.RunInBlockingCharge-
    RunInFATRunInBlockingCharge = glob.glob(f'{data}\\tests\\RunInFAT.RunInBlockingCharge-*')
    result_RunInFATRunInBlockingCharge = 'FAILED'
    for up in RunInFATRunInBlockingCharge:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATRunInBlockingCharge-metadata.txt')
    try:
        with open('result\\RunInFATRunInBlockingCharge-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATRunInBlockingCharge = 'PASSED'
        name_test.append('RunInFAT.RunInBlockingCharge')
        result.append([result_RunInFATRunInBlockingCharge,result_RunInFATRunInBlockingCharge])      
        # print('RunInFATRunInBlockingCharge: '+result_RunInFATRunInBlockingCharge)
    except:
        name_test.append('RunInFAT.RunInBlockingCharge')
        result.append([result_RunInFATRunInBlockingCharge,notest])

    # RunInFAT.Barrier_5-
    RunInFATBarrier_5 = glob.glob(f'{data}\\tests\\RunInFAT.Barrier_5-*')
    result_RunInFATBarrier_5 = 'FAILED'
    for up in RunInFATBarrier_5:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATBarrier_5-metadata.txt')
    try:
        with open('result\\RunInFATBarrier_5-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATBarrier_5 = 'PASSED'
        name_test.append('RunInFAT.Barrier_5')
        result.append([result_RunInFATBarrier_5,result_RunInFATBarrier_5])      
        # print('RunInFATBarrier_5: '+result_RunInFATBarrier_5)
    except:
        name_test.append('RunInFAT.Barrier_5')
        result.append([result_RunInFATBarrier_5,notest])

    ##########################################################################################
    # RunInFAT.Finish-
    RunInFATFinish = glob.glob(f'{data}\\tests\\RunInFAT.Finish-*')
    result_RunInFATFinish = 'FAILED'
    for up in RunInFATFinish:
        shutil.copyfile(f'{up}\\metadata', f'{data}\\result\\RunInFATFinish-metadata.txt')
    try:
        with open('result\\RunInFATFinish-metadata.txt','r') as f:
            texto = f.read()
            if re.findall('status: PASSED',texto):
                result_RunInFATFinish = 'PASSED'    
        # print('RunInFATFinish: '+result_RunInFATFinish)
    except:
        result_RunInFATFinish = 'FAILED'

    ##########################################################################################    

    # Obtener el numero de serie del Archivo UpdateCr50Firmware
    with open('result\\UpdateCr50Firmware-metadata.txt','r') as f:
        texto = f.readlines()
        for x in texto:
            if re.findall("!!python/unicode 'serial_number':",x):
                numero_serie=x[54:77]
                print(numero_serie)

    try:
        api = 'http://production.42-q.com/mes-api/p2581dc1/units/'
        reque = requests.get(api + numero_serie.upper() + '/history')
    except Exception as a:
        print(a)

    #entramos a la api en el diccionario attributes
    attrs = reque.json()['data']['attributes']

    #Comenzamos a traer los datos
    fru = " " 
    part_number = reque.json()['data']['part_number']
    #Recorremos el diccionario, recordar que removed debe ser igual que 0 para yo poder tomarlo
    for att in attrs:   
        if att['removed'] == 0:
            if att["name"] == "FRU":
                fru = att["attr_data"]

    #print(part_number)
    #print(fru)

    dic = dict(zip(name_test,result))
    ''' unzip al diccionarios
    for x in dic:
        print(x)
        print(dic[x])
    '''
    # *** Construccion del XML -> **** 

    #activityKey es la manera que el sistema SFDC toma como id, como no puedo ponerle un ID, vamo a usar fecha en el siguiente formato> 
    activitykey = datetime.datetime.now().strftime("%Y%m%d%S")
    dateTime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    xml = ET.Element("SFDCMeasurement", activityKey=activitykey)

    #Item principales del xml.
    ProcessSessionStart = ET.SubElement(xml, "ProcessSessionStart", sessionId="LVQ0000001", dateTime=dateTime)
    ET.SubElement(ProcessSessionStart, "Product", boardRevision=fru, itemType=part_number)
    ET.SubElement(ProcessSessionStart, "Operator", givenName="Lenovo", employeeId="0000000")
    ET.SubElement(ProcessSessionStart, "Entity", stage="FNT", stationId="FT1")
    ET.SubElement(ProcessSessionStart, "Recipe", revision="1.0", recipeId="100e TEST")

    if result_Finish  == 'PASSED' and result_RunInFATFinish == 'PASSED':
        ET.SubElement(xml, "ItemProcessStatus", comment = 'comment', mode="PRODUCTION", status="PASSED", itemInstanceId=numero_serie)
    else:
        ET.SubElement(xml, "ItemProcessStatus", comment = 'comment', mode="PRODUCTION", status="FAILED", itemInstanceId=numero_serie)


    # FFT.UpdateCr50Firmware.UpdateCR50Firmware
    for x in dic:
        processStep = ET.SubElement(xml, "ProcessStepStatus",  
                        datetime=dateTime, 
                        processStepId=x) 
        meas = ET.SubElement(processStep, "Measurement", 
                        status=dic[x][0], 
                        type=dic[x][1], 
                        measurementId=x)
        ET.SubElement(meas, "ExpectedNumeric", units=dic[x][1])


    #Process Session end agregar al final del xml, Fecha y sessionID
    dateTime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    ET.SubElement(xml, "ProcessSessionEnd", sessionId="LVQ0000001", dateTime=dateTime)


    arbol = ET.ElementTree(xml)
    name_file_xml = (f"FT1-REQUEST_SANMINA_{activitykey}_{numero_serie}")
    arbol.write(f"{name_file_xml}.xml")

    shutil.rmtree('result')
    shutil.rmtree('tests')
    os.rename(provicional, f'{name_file_xml}_Log')   

def select_file():
    filetypes = (('All files', '*.*'),('text files', '*.txt'))
    filename = fd.askopenfilename(title='Pregunta', initialdir='/', filetypes=filetypes)
    log=askyesno(title='Selected File', message='Desea realizar el XML del archivo '+filename)

    if log == True:
        info.set('Generando XML...')
        root.update()
        os.mkdir(provicional)
        os.mkdir('result')
        ruta = os.getcwd()+"\\"+provicional

        shutil.unpack_archive(filename,ruta)
        shutil.copytree(f'{provicional}\\var\\factory\\tests',f'{data}\\tests')

        archivos_txt()
        info.set('Open a file')
        root.update()


# open button
btn_font = Font(family="Roboto Cn", size=20)
open_button = tk.Button(root, textvariable=info, 
                        command=select_file, 
                        width=50, height=15, 
                        borderwidth=10,
                        font=btn_font)
open_button.pack(expand=True)


# run the application
root.mainloop()
