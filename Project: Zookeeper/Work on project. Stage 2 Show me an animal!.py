'''Description
One of the most important parts of working with animals is keeping an eye on them. We need to see the animals on the screen to know how they are doing, right? Now we are ready to print something awesome: an image of an animal!

Objectives
For the second stage, you will need to develop an animal printer. Your program should display the animal identified in the code field.

Please, don't remove the r character at the start of the code template. It's a part of the string and it's important. So, the string should start with r""" sequence. This “r” at the beginning stands for “raw” and allows various characters to be used in a string without escaping. For instance, “\” in a non-raw string should be escaped as follows: “\\”.

Example
Your output should contain the following ASCII image:

Switching on the camera in the camel habitat...
'''
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that! Our little camel is sunbathing!

'''
    
print(r"""
Switching on the camera in the camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that! Our little camel is sunbathing!""")