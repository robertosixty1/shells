#!/bin/bash

if [ -f ~/.bashrc ]; then
    mv ~/.bashrc ~/.bashrc.old
fi

if [ -f ~/.zshrc ]; then
    mv ~/.zshrc ~/.zshrc.old
fi

ln -sf ./.bashrc ~/.bashrc
ln -sf ./.zshrc ~/.zshrc