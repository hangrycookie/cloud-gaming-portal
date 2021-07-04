"""Create and manage virtual machines."""

import traceback

from azure.mgmt.compute import ComputeManagementClient
from msrestazure.azure_exceptions import CloudError
from config import get_credentials, GROUP_NAME, VM_NAME


def start_vm(vm_number):
    """Virtual Machine management example."""
    #
    # Create all clients with an Application (service principal) token provider
    #
    credentials, subscription_id = get_credentials()
    # resource_client = ResourceManagementClient(credentials, subscription_id)
    compute_client = ComputeManagementClient(credentials, subscription_id)
    # network_client = NetworkManagementClient(credentials, subscription_id)

    ###########
    # Prepare #
    ###########

    try:

        # Start the VM
        print('\nStart VM')
        async_vm_start = compute_client.virtual_machines.start(
            GROUP_NAME, VM_NAME[vm_number])
        async_vm_start.wait()

    except CloudError:
        print('A VM operation failed:\n{}'.format(traceback.format_exc()))
        return False
    else:
        print('All example operations completed successfully!')
        return True
    finally:
        pass


def stop_vm(vm_number):
    """Virtual Machine management example."""
    #
    # Create all clients with an Application (service principal) token provider
    #
    credentials, subscription_id = get_credentials()
    # resource_client = ResourceManagementClient(credentials, subscription_id)
    compute_client = ComputeManagementClient(credentials, subscription_id)
    # network_client = NetworkManagementClient(credentials, subscription_id)

    ###########
    # Prepare #
    ###########

    try:

        # Stop the VM

        print('\nStop VM')
        async_vm_stop = compute_client.virtual_machines.power_off(
            GROUP_NAME, VM_NAME[vm_number])
        async_vm_stop.wait()

        print('\nDeallocate VM')
        async_vm_deallocate = compute_client.virtual_machines.deallocate(
            GROUP_NAME, VM_NAME[vm_number])
        async_vm_deallocate.wait()

    except CloudError:
        print('A VM operation failed:\n{}'.format(traceback.format_exc()))
        return False
    else:
        print('All example operations completed successfully!')
        return True


if __name__ == "__main__":
    start_vm()
