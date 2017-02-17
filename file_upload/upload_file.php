<?php


print_r(__FILE__);

//会打印出:C:\xampp\htdocs\3\runoob\php_file\file_upload\upload_file.php,即当前这个文件的位置,当然和这里的内容没啥关系了,只是爽哥为了温习


echo '<br>';
echo '<br>';
echo '<br>';

if ($_FILES['file']['error']>0)
{
    echo '错误:'.$_FILES['file']['error'].'<br>';

}
else
{

    echo '上传文件名:'.$_FILES['file']['name'].'<br>';
    echo '文件类型:'.$_FILES['file']['type'].'<br>';
    echo '文件大小:'.($_FILES['file']['size']/1024).'kb<br>';
    echo '文件临时存储的位置:'.$_FILES['file']['tmp_name'];

}




