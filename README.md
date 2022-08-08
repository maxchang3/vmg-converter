# vmg-convert

> VMG (vMessage) is a file format used by Nokia phones. VMG files store by default sent and received SMS messages. Single VMG files contains the actual text of SMS message and related metadata, such as information about the sender, and date sent or received.

Convert .vmg file into popular formats. Now only to .xml (Android SMS).

# Usage
## Install
```properties
git clone https://github.com/MaxChang3/vmg-converter
cd vmg-converter
pip install -r requirements.txt
```
## Convert

```properties
python vmg-converter.py you-vmg-file.vmg
```

for example, we have a vmg file here:

```properties
BEGIN:VMSG
VERSION: 1.1
X-IRMS-TYPE:SMS
X-MESSAGE-TYPE:DELIVER
X-MA-TYPE:-1
BEGIN:VCARD
VERSION: 2.1
TEL:383816
END:VCARD
BEGIN:VENV
BEGIN:VBODY
Date:1451393917000
Hello World!
END:VBODY
END:VENV
END:VMSG
```

we can use the command above convert it to

```xml
<?xml version='1.0' encoding='utf-8'?>
<smses count="1">
	<sms protocol="0" address="383816" date="1451393917000" type="1" body="Hello World!"></sms>
</smses>
```

Note that data in `VBODY` is quite different on various devices. So you need to add custom params according to your file structure, for example, some phones show `Date` as this(without the colon):

```properties
BEGIN:VBODY
Date 1451393917000
Hello World!
END:VBODY
```
So you need run this

```properties
python vmg-converter.py you-vmg-file.vmg -f "Data "
```

Or, if you want to parse the "Subject:" param in the 'VBODY', just add: `-f "Subject:"` (**WIP** for other params except "Date ")

## Import xml

For Android, I recommend "SMS Backup and Restore".


# Reference:

https://matteocontrini.medium.com/how-to-transfer-windows-phone-smses-to-android-6d5e941f3362

https://github.com/matteocontrini/sms-wp-to-android
