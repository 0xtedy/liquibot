from web3 import Web3
import abi
import const
import time

polygon = "https://polygon-rpc.com/"
web3 = Web3(Web3.HTTPProvider(polygon))

#pbladdress = web3.toChecksumAddress(str(input("Enter your public address: ")))

#prvaddress = str(input("Enter your private key (dont worry she will not be stored): "))

vaultRouterAddressWETH = '0x3fd939B017b31eaADF9ae50C7fF7Fa5c0661d47C'

def checkLiquidation(_vaultID, _vaultAddress):
    vault_contract = web3.eth.contract(address=_vaultAddress, abi=abi.MAIvaultABI)
    return vault_contract.functions.checkLiquidation(_vaultID).call()

def vaultCount(_vaultAddress):
    vault_contract = web3.eth.contract(address=_vaultAddress, abi=abi.MAIvaultABI)
    return vault_contract.functions.vaultCount().call()

def checkRatio(_vaultID, _vaultAddress):
    vault_contract = web3.eth.contract(address=_vaultAddress, abi=abi.MAIvaultABI)
    return vault_contract.functions.checkCollateralPercentage(_vaultID).call()

def findRiskyVault(_vaultAddress):
    riskyvaults = []
    vault_contract = web3.eth.contract(address=_vaultAddress, abi=abi.MAIvaultABI)
    print("looking for risky vault 👀",vaultCount(_vaultAddress),"left")
    for id in range(1, vaultCount(_vaultAddress)):
        try:
            if checkRatio(id, _vaultAddress) <= 120 and checkRatio(id, _vaultAddress) != 0:
                print(id)
                riskyvaults.append(id)
        except Exception as e:
            print("Error", e.__class__, "occurred.")
    return riskyvaults

ls = [const.MAIVaultAddressWETH[0], const.MAIVaultAddressGHST[0], const.MAIVaultAddressBAL[0],  const.MAIVaultAddressCRV[0],  const.MAIVaultAddressBTC[0]]
ns = [const.MAIVaultAddressWETH[1], const.MAIVaultAddressGHST[1], const.MAIVaultAddressBAL[1],  const.MAIVaultAddressCRV[1],  const.MAIVaultAddressBTC[1]]
lis = {}


for x in range(len(ls)):
    lis[ns[x]] = findRiskyVault(ls[x])

print(lis)

# print(vaultCount(vaultRouterAddressWETH), "vault open")
# for id in range(600, vaultCount(vaultRouterAddressWETH)):
#     try:
#         if checkLiquidation(id, const.MAIVaultAddressWETH) == True:
#             print(id, "liquidable !")
#             break
#         else:
#             print(id, "healthy")
#     except Exception as e:
#         print("Error", e.__class__, "occurred.")

