from web3 import Web3
import abi
import time

polygon = "https://polygon-rpc.com/"
web3 = Web3(Web3.HTTPProvider(polygon))

pbladdress = web3.toChecksumAddress(str(input("Enter your public address: ")))

#prvaddress = str(input("Enter your private key (dont worry she will not be stored): "))

vaultRouterAddressWETH = '0x3fd939B017b31eaADF9ae50C7fF7Fa5c0661d47C'


def checkLiquidation(_vaultID):
    vault_contract = web3.eth.contract(address=vaultRouterAddressWETH, abi=abi.WETHvaultABI)
    return vault_contract.functions.checkLiquidation(_vaultID).call()

def vaultCount(_vaultAddress):
    vault_contract = web3.eth.contract(address=_vaultAddress, abi=abi.WETHvaultABI)
    return vault_contract.functions.vaultCount().call()

print(vaultCount(vaultRouterAddressWETH), "vault open")
for id in range(600, vaultCount(vaultRouterAddressWETH)):
    try:
        if checkLiquidation(id) == True:
            print(id, "liquidable !")
            break
        else:
            print(id, "healthy")
    except Exception as e:
        print("Error", e.__class__, "occurred.")

