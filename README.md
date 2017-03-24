Deadlinks crawler	
========================

There are several ways to implement website crawler. I mean Synchronous and Asynchronous arch, or regular http requests and PhantomJS (or other rendering engines). Or we can use threads. Due to the fact that nothing about it in tech reqirements I decided to make it pretty simple. It is not for production use because it is pretty slow (it uses regular "blocking" requests).