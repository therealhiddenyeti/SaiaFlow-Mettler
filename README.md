# SaisFlow-Mettler

  

This repository contains the following:

> role/saia-flow
   
> site.yml
   
>>- used to execute the role saia flow
>
> saia-flow-cleanup.yml
   
>>	- polls the /opt/saia_flow/processed directory for files more than 30 minutes old
   
> 	saia-flow-error-finder.yml
   
>> - polls the /opt/saia_flow/errors directory for files. If files are found, the play fails and a notification can be generated.
   
> saia-flow-error-handler.yml
>>- reprocessed the files in the /opt/saia_flow/errors directory by moving them back to the incoming folder.
   
> saia-flow-tester.yml
   
>> - this play will generate randoming sized files, at random intervals, in the /opt/saia_flow/incoming directory.

## Requirements

------------

  

See the README.md of the role saia-flow

  

## Role Variables

--------------

See the README.md of the role saia-flow

  

## Dependencies

------------

  

No additional Ansible dependancies

  

## License

-------

  

BSD

  

## Author Information

------------------

  

Thomas Gould