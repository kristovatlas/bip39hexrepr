# bip39hexrepr

Convert BIP39 phrase to succinct hex format and vice versa.

## Usage

```
Usage:

$ python3 bip39_hex_convert.py "exile credit explain garden question problem such virtual pride caution real health until still wire calm title famous return practice panic culture jungle clinic"
exile credit explain garden question problem such virtual pride caution real health until still wire calm title famous return practice panic culture jungle clinic
=>
27d1982842fd57c55b6c37a35541255973517716ae7e11047172955c154b4fd1ac3c8159
```

```
$ python3 bip39_hex_convert.py "27d1982842fd57c55b6c37a35541255973517716ae7e11047172955c154b4fd1ac3c8159"
27d1982842fd57c55b6c37a35541255973517716ae7e11047172955c154b4fd1ac3c8159
=>
exile credit explain garden question problem such virtual pride caution real health until still wire calm title famous return practice panic culture jungle clinic
```

## Example Use Case

With: https://github.com/trezor/python-shamir-mnemonic/

1. Convert BIP39 phrase to hex:
```
$ python3 bip39_hex_convert.py "exile credit explain garden question problem such virtual pride caution real health until still wire calm title famous return practice panic culture jungle clinic"
exile credit explain garden question problem such virtual pride caution real health until still wire calm title famous return practice panic culture jungle clinic
=>
27d1982842fd57c55b6c37a35541255973517716ae7e11047172955c154b4fd1ac3c8159
```

2. Create Shamir's shards:
```
$ shamir create 2of3 --master-secret=27d1982842fd57c55b6c37a35541255973517716ae7e11047172955c154b4fd1ac3c8159
Using master secret: 27d1982842fd57c55b6c37a35541255973517716ae7e11047172955c154b4fd1ac3c8159
Group 1 of 1 - 2 of 3 shares required:
shadow corner academic acid depart velvet crucial tolerate biology satisfy knife evening acid lamp volume dominant gray organize capital mother luxury listen testify wisdom pants adorn hour drove genuine briefing pajamas calcium preach award aunt makeup
shadow corner academic agency alto problem priority grasp voting evil reject nylon drove thank unfold artist club medical academic emperor junk ultimate broken infant easel chest total human taxi wireless loyalty cleanup smug campus idle dramatic
shadow corner academic always buyer escape class facility mouse script vocal transfer dress game platform firefly that remember eraser loud cowboy flavor laden example furl elbow ladle news glance scramble tricycle sister sugar dish that nylon
```

3. Restore shards:
```
$ shamir recover
Enter a recovery share: shadow corner academic acid depart velvet crucial tolerate biology satisfy knife evening acid lamp volume dominant gray organize capital mother luxury listen testify wisdom pants adorn hour drove genuine briefing pajamas calcium preach award aunt makeup

● 1 of 2 shares needed from group shadow corner academic
Enter a recovery share: shadow corner academic agency alto problem priority grasp voting evil reject nylon drove thank unfold artist club medical academic emperor junk ultimate broken infant easel chest total human taxi wireless loyalty cleanup smug campus idle dramatic

✓ 2 of 2 shares needed from group shadow corner academic
SUCCESS!
Your master secret is: 27d1982842fd57c55b6c37a35541255973517716ae7e11047172955c154b4fd1ac3c8159
```

4. Convert back to BIP39 phrase:
```
$ python3 bip39_hex_convert.py 27d1982842fd57c55b6c37a35541255973517716ae7e11047172955c154b4fd1ac3c8159
27d1982842fd57c55b6c37a35541255973517716ae7e11047172955c154b4fd1ac3c8159
=>
exile credit explain garden question problem such virtual pride caution real health until still wire calm title famous return practice panic culture jungle clinic
```
